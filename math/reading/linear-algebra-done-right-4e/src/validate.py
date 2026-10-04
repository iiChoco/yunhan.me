"""Audit generated content and run the site's checker and renderer.

An incomplete book is explicitly reported as incomplete. No placeholder sections
are created merely to make the full-book checker pass.
"""
import argparse
import ast
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--label',default='current')
    args=parser.parse_args()
    book=json.loads((ROOT/'book.json').read_text())
    expected=[s['id'] for c in book['chapters'] for s in c['sections']]
    sections={p.stem:json.loads(p.read_text()) for p in (ROOT/'sections').glob('*.json')}
    errors=[]
    ids=set()
    earlier={}
    chapter_of={s['id']:c['id'] for c in book['chapters'] for s in c['sections']}
    graph={c['id']:c['requires'] for c in book['chapters']}
    def ancestors(cid):
        result=set(graph[cid])
        for parent in graph[cid]: result |= ancestors(parent)
        return result
    for sid in expected:
        if sid not in sections: continue
        sec=sections[sid]
        cid=chapter_of[sid]
        if not 4 <= len(sec['cards']) <= 10: errors.append(f'{sid}: needs 4–10 cards')
        if not sec['blocks'] or sec['blocks'][0]['kind']!='prose': errors.append(f'{sid}: missing opening prose')
        if sid.endswith('-exercises'):
            ex=[b for b in sec['blocks'] if b['kind']=='exercise']
            if not 14<=len(ex)<=20: errors.append(f'{sid}: needs 14–20 exercises')
            if any(not b.get('optional') for b in ex): errors.append(f'{sid}: nonoptional exercise')
        for block_index,b in enumerate(sec['blocks']):
            bid=b['id']
            if bid in ids: errors.append(f'{bid}: repeated id')
            ids.add(bid)
            if not re.fullmatch(cid+r'-[a-z0-9-]+',bid): errors.append(f'{bid}: malformed id')
            if not b.get('title'): errors.append(f'{bid}: missing title')
            if b['kind'] in ('theorem','lemma','proposition','corollary','example','exercise') and 'proof' not in b:
                following=sec['blocks'][block_index+1:block_index+2]
                if not following or following[0]['kind']!='remark' or 'faith' not in following[0]['tex'].lower(): errors.append(f'{bid}: unproved result lacks immediate faith remark')
            if 'proof' in b:
                if b['kind'] in ('prose','definition','remark'): errors.append(f'{bid}: proof on nonprovable block')
                if b.get('difficulty') not in range(1,6) or b.get('minutes',0)<=0: errors.append(f'{bid}: invalid effort metadata')
                if not 1<=len(b.get('hints',[]))<=3: errors.append(f'{bid}: needs 1–3 hints')
                if re.search(r'\bclearly\b',b['proof'],re.I): errors.append(f'{bid}: uses clearly')
                for used in b.get('uses',[]):
                    if used not in earlier: errors.append(f'{bid}: unavailable dependency {used}'); continue
                    uc,ub=earlier[used]
                    if uc!=cid and uc not in ancestors(cid): errors.append(f'{bid}: chapter prerequisite missing for {used}')
                    if ub.get('optional'): errors.append(f'{bid}: relies on optional exercise {used}')
            earlier[bid]=(cid,b)
            fragments=[b.get('tex',''),b.get('proof','')]+b.get('hints',[])
            for fragment in fragments:
                if re.search(r'\\(?:label|ref|tag)\b|\\begin\{(?:proof|theorem|tikzpicture)\}',fragment): errors.append(f'{bid}: forbidden LaTeX')
                if re.search('[\u2200-\u22ff\u27c0-\u27ef\U0001d400-\U0001d7ff]',fragment): errors.append(f'{bid}: Unicode mathematics')
        for card in sec['cards']:
            if card['id'] in ids: errors.append(f"{card['id']}: repeated id")
            ids.add(card['id'])
            if card.get('item') not in {b['id'] for b in sec['blocks']}: errors.append(f"{card['id']}: invalid item")
    for p in (ROOT/'src').glob('*.py'):
        source=p.read_text()
        tree=ast.parse(source,filename=str(p))
        if p.stem in ('common','book','validate'): continue
        for node in ast.walk(tree):
            if not isinstance(node,ast.Call) or not isinstance(node.func,ast.Attribute): continue
            positions={'p':[2],'note':[2],'d':[2],'r':[2,3,6],'card':[2,3],'add':[3]}.get(node.func.attr,[])
            targets=[node.args[i] for i in positions if len(node.args)>i]
            targets += [kw.value for kw in node.keywords if kw.arg in ('tex','proof','hints','front','back')]
            for target in targets:
                for literal in ast.walk(target):
                    if isinstance(literal,ast.Constant) and isinstance(literal.value,str):
                        spelling=ast.get_source_segment(source,literal)
                        if spelling and not spelling.lower().startswith('r'): errors.append(f'{p.name}:{literal.lineno}: LaTeX field is not a raw string')
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',UV_CACHE_DIR=str(ROOT/'work'/'uv-cache'))
    check=subprocess.run(['uv','run','--no-sync','python','../scripts/reading_module.py','check',str(ROOT)],cwd=REPO/'door',env=env,text=True,capture_output=True)
    render=subprocess.run(['node','scripts/reading_render.mjs',str(ROOT)],cwd=REPO,env=env,text=True,capture_output=True)
    log='CONTENT AUDIT\n'+('\n'.join(errors) if errors else 'PASS')+'\nSITE CHECKER\n'+check.stdout+check.stderr+'\nSITE RENDERER\n'+render.stdout+render.stderr+f'\nRenderer exit: {render.returncode}\n'
    (ROOT/'work'/f'check-{args.label}.txt').write_text(log)
    unexpected=[line for line in (check.stdout+check.stderr).splitlines() if line.strip() and 'is in the manifest but has no file' not in line and not re.match(r'\d+ problems? in ',line)]
    print(f"{len(sections)}/{len(expected)} sections; {sum(len(s['blocks']) for s in sections.values())} blocks; {sum('proof' in b for s in sections.values() for b in s['blocks'])} proofs; {sum(len(s['cards']) for s in sections.values())} cards")
    print(f'Content audit: {len(errors)} errors; renderer exit: {render.returncode}; missing sections: {len(set(expected)-set(sections))}')
    for line in errors+unexpected: print(line)
    if render.returncode: print(render.stdout+render.stderr)
    if errors or render.returncode or (check.returncode and unexpected): return 1
    if len(sections)==len(expected): print(check.stdout.strip())
    return 0

if __name__=='__main__': sys.exit(main())
