"""Shared helpers for the chapter 3 section scripts."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path("/Users/choco/Projects/yunhan.me/math/reading/pugh-rma/sections")


def text(kind: str, id: str, tex: str, title: str = "") -> dict:
    block = {"id": id, "kind": kind, "number": "", "tex": tex.strip()}
    if title:
        block["title"] = title
    return block


def prose(id: str, tex: str) -> dict:
    return text("prose", id, tex)


def remark(id: str, tex: str, title: str = "") -> dict:
    return text("remark", id, tex, title)


def example(id: str, tex: str, title: str = "") -> dict:
    return text("example", id, tex, title)


def definition(id: str, title: str, tex: str) -> dict:
    return text("definition", id, tex, title)


def stated(kind: str, id: str, title: str, tex: str) -> dict:
    return text(kind, id, tex, title)


def gate(kind: str, id: str, title: str, tex: str, proof: str, difficulty: int, minutes: int, hints: list[str], uses: list[str]) -> dict:
    return {"id": id, "kind": kind, "number": "", "title": title, "tex": tex.strip(), "proof": proof.strip(),
            "difficulty": difficulty, "minutes": minutes, "hints": [h.strip() for h in hints], "uses": uses}


def card(id: str, front: str, back: str, item: str = "") -> dict:
    c = {"id": id, "front": front.strip(), "back": back.strip()}
    if item:
        c["item"] = item
    return c


def write(section_id: str, blocks: list[dict], cards: list[dict]) -> None:
    path = OUT / f"{section_id}.json"
    with path.open("w", encoding="utf-8") as fh:
        json.dump({"version": 1, "id": section_id, "blocks": blocks, "cards": cards}, fh, indent=1, ensure_ascii=False)
    gates = sum(1 for b in blocks if "proof" in b)
    print(f"{section_id}: {len(blocks)} blocks, {gates} provable, {len(cards)} cards")
