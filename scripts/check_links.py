#!/usr/bin/env python3
from __future__ import annotations
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
links = []
for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if link.startswith("#"):
            continue
        links.append((str(md.relative_to(ROOT)), link))

seen = set()
dupes = []
for _, link in links:
    if link in seen:
        dupes.append(link)
    seen.add(link)

print(f"Markdown links: {len(links)}")
print(f"Unique links: {len(seen)}")
print(f"Duplicate links: {len(set(dupes))}")
