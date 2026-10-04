"""Shared builder for the chapter 2 section scripts (Pugh reading module)."""
from __future__ import annotations

import json

OUT = "/Users/choco/Projects/yunhan.me/math/reading/pugh-rma/sections/"


class Section:
    def __init__(self, id: str) -> None:
        self.id = id
        self.blocks: list[dict] = []
        self.cards: list[dict] = []

    def _plain(self, kind: str, id: str, tex: str, title: str = "") -> None:
        b = {"id": id, "kind": kind}
        if kind != "prose":
            b["number"] = ""
            if title:
                b["title"] = title
        b["tex"] = tex.strip()
        self.blocks.append(b)

    def p(self, id: str, tex: str) -> None:
        self._plain("prose", id, tex)

    def r(self, id: str, tex: str, title: str = "") -> None:
        self._plain("remark", id, tex, title)

    def e(self, id: str, title: str, tex: str) -> None:
        self._plain("example", id, tex, title)

    def d(self, id: str, title: str, tex: str) -> None:
        self._plain("definition", id, tex, title)

    def stated(self, kind: str, id: str, title: str, tex: str) -> None:
        self._plain(kind, id, tex, title)

    def t(self, kind: str, id: str, title: str, tex: str, proof: str, difficulty: int,
          minutes: int, hints: list[str], uses: list[str]) -> None:
        self.blocks.append({"id": id, "kind": kind, "number": "", "title": title, "tex": tex.strip(),
                            "proof": proof.strip(), "difficulty": difficulty, "minutes": minutes,
                            "hints": [h.strip() for h in hints], "uses": uses})

    def card(self, id: str, front: str, back: str, item: str | None = None) -> None:
        c = {"id": id}
        if item:
            c["item"] = item
        c["front"] = front.strip()
        c["back"] = back.strip()
        self.cards.append(c)

    def write(self) -> None:
        with open(OUT + self.id + ".json", "w") as f:
            json.dump({"version": 1, "id": self.id, "blocks": self.blocks, "cards": self.cards},
                      f, indent=1, ensure_ascii=False)
        gates = sum(1 for b in self.blocks if "proof" in b)
        print(f"{self.id}: {len(self.blocks)} blocks, {gates} provable, {len(self.cards)} cards")
