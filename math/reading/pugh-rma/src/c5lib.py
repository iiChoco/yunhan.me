"""Shared builder for the chapter 5 section scripts."""
import json, re

OUT = "/Users/choco/Projects/yunhan.me/math/reading/pugh-rma/sections/"


class Section:
    def __init__(self, sid):
        self.sid, self.blocks, self.cards = sid, [], []

    def _t(self, s):
        return re.sub(r"[ \t]*\n[ \t]*", " ", s.strip())

    def b(self, id, kind, tex, title="", proof=None, d=None, m=None, hints=None, uses=None):
        blk = {"id": "c5-" + id, "kind": kind, "number": "", "title": title, "tex": self._t(tex)}
        if not title:
            del blk["title"]
        if proof is not None:
            blk["proof"] = self._t(proof)
            blk["difficulty"] = d
            blk["minutes"] = m
            blk["hints"] = [self._t(h) for h in (hints or [])]
            blk["uses"] = ["c5-" + u for u in (uses or [])]
        self.blocks.append(blk)

    def c(self, id, front, back, item=None):
        card = {"id": "c5-card-" + id}
        if item:
            card["item"] = "c5-" + item
        card["front"] = self._t(front)
        card["back"] = self._t(back)
        self.cards.append(card)

    def write(self):
        with open(OUT + self.sid + ".json", "w") as f:
            json.dump({"version": 1, "id": self.sid, "blocks": self.blocks, "cards": self.cards}, f, indent=1, ensure_ascii=False)
        n = sum(1 for b in self.blocks if "proof" in b)
        print(self.sid, len(self.blocks), "blocks", n, "provable", len(self.cards), "cards")
