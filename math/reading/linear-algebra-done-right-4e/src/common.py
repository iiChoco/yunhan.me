"""Small serialization helper; all mathematical content lives in section scripts."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class Section:
    def __init__(self, sid):
        self.sid = sid
        self.prefix = 'c' + sid.split('-')[0].rstrip('abcdef') + '-'
        self.data = dict(version=1,id=sid,blocks=[],cards=[])
    def full(self, name):
        return name if name.startswith('c') and '-' in name and name[1:name.index('-')].isdigit() else self.prefix+name
    def add(self, kind, name, title, tex, number='', page=''):
        b = dict(id=self.full(name),kind=kind,number=number,title=title,tex=tex.strip())
        if page: b['page']=str(page)
        self.data['blocks'].append(b)
        return b
    def d(self,name,title,tex,number='',page=''):
        return self.add('definition',name,title,tex,number,page)
    def p(self,name,title,tex,page=''):
        return self.add('prose',name,title,tex,page=page)
    def note(self,name,title,tex,page=''):
        return self.add('remark',name,title,tex,page=page)
    def r(self,name,title,tex,proof,difficulty,minutes,hints,uses,number='',page='',kind='theorem',optional=False):
        b=self.add(kind,name,title,tex,number,page)
        b.update(proof=proof.strip(),difficulty=difficulty,minutes=minutes,hints=[h.strip() for h in hints],uses=[self.full(u) for u in uses],optional=optional)
        return b
    def card(self,name,item,front,back):
        self.data['cards'].append(dict(id=self.full('card-'+name),item=self.full(item),front=front.strip(),back=back.strip()))
    def write(self):
        target=ROOT/'sections'/f'{self.sid}.json'
        target.parent.mkdir(exist_ok=True)
        with target.open('w',encoding='utf-8') as f:
            json.dump(self.data,f,indent=1,ensure_ascii=False)
            f.write('\n')
