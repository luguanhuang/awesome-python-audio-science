#!/usr/bin/env python3
from __future__ import annotations
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "CHANGELOG.md",
    "docs/tizwildin-ecosystem-routing-map.md",
    "data/resources.json",
    "data/seo_keywords.json",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("Missing required files:", missing)
    sys.exit(1)

for fp in [ROOT / "data/resources.json", ROOT / "data/seo_keywords.json"]:
    json.loads(fp.read_text(encoding="utf-8"))

readme = (ROOT / "README.md").read_text(encoding="utf-8")
markers = [
    "Awesome Python Audio Science",
    "TizWildinEntertainmentHUB",
    "TizWildin HUB public router",
    "deconstructed loops",
    "awesome-audio-lists",
    "awesome-music-platforms",
    "FreeEQ8",
    "FreeVox8",
]
failed = [m for m in markers if m not in readme]
if failed:
    print("Missing README markers:", failed)
    sys.exit(1)

links = re.findall(r"https?://[^)\s]+", readme)
if len(set(links)) < 25:
    print("Expected more public links, found", len(set(links)))
    sys.exit(1)

print("Validation OK")
