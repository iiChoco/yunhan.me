"""Shared builders for the chapter 6 section scripts."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path("/Users/choco/Projects/yunhan.me/math/reading/pugh-rma/sections")


def _clean(s: str) -> str:
    return s.strip()


def prose(id: str, tex: str) -> dict:
    return {"id": id, "kind": "prose", "tex": _clean(tex)}


def note(kind: str, id: str, title: str, tex: str) -> dict:
    """definition / remark / example / unproved theorem."""
    return {"id": id, "kind": kind, "number": "", "title": title, "tex": _clean(tex)}


def result(kind: str, id: str, title: str, tex: str, proof: str, difficulty: int,
           minutes: int, hints: list[str], uses: list[str]) -> dict:
    return {"id": id, "kind": kind, "number": "", "title": title, "tex": _clean(tex),
            "proof": _clean(proof), "difficulty": difficulty, "minutes": minutes,
            "hints": [_clean(h) for h in hints], "uses": uses}


def card(id: str, item: str | None, front: str, back: str) -> dict:
    c = {"id": id, "front": _clean(front), "back": _clean(back)}
    if item:
        c["item"] = item
    return c


def write(section: str, blocks: list[dict], cards: list[dict]) -> None:
    ids = [b["id"] for b in blocks] + [c["id"] for c in cards]
    assert len(ids) == len(set(ids)), "duplicate id"
    assert all(i.startswith("c6-") for i in ids)
    with open(OUT / f"{section}.json", "w") as fh:
        json.dump({"version": 1, "id": section, "blocks": blocks, "cards": cards}, fh, indent=1, ensure_ascii=False)
    provable = sum(1 for b in blocks if "proof" in b)
    print(f"{section}: {len(blocks)} blocks, {provable} provable, {len(cards)} cards")
