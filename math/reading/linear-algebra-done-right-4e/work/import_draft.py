"""Import a reviewed draft from this task's own agent messages."""
import ast
import json
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[1]
sid,author=sys.argv[1:]
logs=Path('/Users/choco/.codex/sessions/2026/10/03').glob('*01a104fa-0d09-7a31-9139-8134fda3912f*')
candidates=[]
for path in logs:
    for line in path.open():
        event=json.loads(line)
        payload=event.get('payload',{})
        if payload.get('type')!='agent_message' or payload.get('author')!='/root/'+author: continue
        for part in payload.get('content',[]):
            text=part.get('text','')
            if 'Message Type: FINAL_ANSWER' not in text: continue
            scripts=re.findall(r'```python\n(.*?)```',text,re.S)
            if not scripts and 'from common import Section' in text:
                scripts=[text[text.index('from common import Section'):]]
            for script in scripts:
                if re.search(r"Section\(['\"]"+re.escape(sid)+r"['\"]\)",script):
                    candidates.append((event.get('timestamp',''),script))
if not candidates: raise SystemExit('No reviewed draft found for '+sid)
source=sorted(candidates)[-1][1]
# The 1C draft's card fragments used single quotes across physical newlines.
if sid=='1c':
    head,sep,tail=source.partition('s.card(')
    tail=re.sub(r"r'([^']*)'",lambda m:"r'''"+m.group(1)+"'''" if '\n' in m.group(1) else m.group(0),tail)
    source=head+sep+tail
if sid in ('3f','7b'):
    def quote_line(match):
        return match[1]+"r"+chr(39)*3+match[2]+chr(39)*3+match[3]
    source=re.sub(r"(?m)^(\s*\[?)r'(?!'')(.*)'(\]?,?)[ \t]*$",quote_line,source)
ast.parse(source)
path=ROOT/'src'/(sid+'.py')
if path.exists(): raise SystemExit('Refusing to overwrite existing source: '+str(path))
path.write_text(source,encoding='utf-8')
print('Imported',sid,'from',author)
