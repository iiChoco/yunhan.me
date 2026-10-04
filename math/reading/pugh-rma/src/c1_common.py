"""Shared builder for the chapter 1 section scripts (ids are prefixed c1-)."""
from __future__ import annotations
import json, pathlib

OUT = pathlib.Path("/Users/choco/Projects/yunhan.me/math/reading/pugh-rma/sections")
P = "c1-"


class Section:
    def __init__(self, sid: str) -> None:
        self.sid = sid
        self.blocks: list[dict] = []
        self.cards: list[dict] = []

    def text(self, id: str, kind: str, tex: str, title: str | None = None) -> None:
        b = {"id": P + id, "kind": kind}
        if title is not None:
            b["number"] = ""
            b["title"] = title
        b["tex"] = tex.strip()
        self.blocks.append(b)

    def prose(self, id, tex): self.text(id, "prose", tex)
    def remark(self, id, tex, title=None): self.text(id, "remark", tex, title)
    def example(self, id, tex, title=None): self.text(id, "example", tex, title)
    def definition(self, id, title, tex): self.text(id, "definition", tex, title)

    def result(self, id: str, kind: str, title: str, tex: str, proof: str, d: int, m: int,
               hints: list[str], uses: list[str] | None = None) -> None:
        b = {"id": P + id, "kind": kind, "number": "", "title": title, "tex": tex.strip(),
             "proof": proof.strip(), "difficulty": d, "minutes": m,
             "hints": [h.strip() for h in hints], "uses": [P + u for u in (uses or [])]}
        self.blocks.append(b)

    def card(self, id: str, front: str, back: str, item: str | None = None) -> None:
        c = {"id": P + "card-" + id}
        if item:
            c["item"] = P + item
        c["front"] = front.strip()
        c["back"] = back.strip()
        self.cards.append(c)

    def write(self) -> None:
        ids = [b["id"] for b in self.blocks]
        assert len(ids) == len(set(ids)), "duplicate ids"
        data = {"version": 1, "id": self.sid, "blocks": self.blocks, "cards": self.cards}
        with open(OUT / f"{self.sid}.json", "w") as f:
            json.dump(data, f, indent=1, ensure_ascii=False)
        prov = sum(1 for b in self.blocks if "proof" in b)
        print(f"{self.sid}: {len(self.blocks)} blocks, {prov} provable, {len(self.cards)} cards")
