"""Shared builder for the Chapter 4 section scripts (4-*.py)."""
import json, os

OUT = "/Users/choco/Projects/yunhan.me/math/reading/pugh-rma/sections"


class Section:
    def __init__(self, sid):
        self.sid, self.blocks, self.cards = sid, [], []

    def text(self, bid, kind, tex, title=""):
        b = {"id": bid, "kind": kind, "number": "", "title": title, "tex": tex.strip()}
        if not title:
            del b["title"]
        self.blocks.append(b)

    def gate(self, bid, kind, title, tex, proof, difficulty, minutes, hints, uses=()):
        self.blocks.append({"id": bid, "kind": kind, "number": "", "title": title,
                            "tex": tex.strip(), "proof": proof.strip(),
                            "difficulty": difficulty, "minutes": minutes,
                            "hints": [h.strip() for h in hints], "uses": list(uses)})

    def card(self, cid, front, back, item=None):
        c = {"id": cid, "front": front.strip(), "back": back.strip()}
        if item:
            c["item"] = item
        self.cards.append(c)

    def write(self):
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, self.sid + ".json"), "w") as fh:
            json.dump({"version": 1, "id": self.sid, "blocks": self.blocks, "cards": self.cards},
                      fh, indent=1, ensure_ascii=False)
        gates = sum(1 for b in self.blocks if "proof" in b)
        print(f"{self.sid}: {len(self.blocks)} blocks, {gates} provable, {len(self.cards)} cards")
