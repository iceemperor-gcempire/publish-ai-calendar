#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = ROOT / "images"
DATA_DIR = ROOT / "data"
PATTERN = re.compile(r"^cal2025_(\d{5})\.jpg$")


def build_items() -> list[dict]:
    items = []
    for file in sorted(IMAGES_DIR.iterdir()):
        if not file.is_file():
            continue
        match = PATTERN.match(file.name)
        if not match:
            continue
        index = int(match.group(1))
        month = f"2025-{index:02d}"
        items.append(
            {
                "id": file.stem,
                "month": month,
                "brand": "aical",
                "variant": 1,
                "ratio_code": "43",
                "ratio": "4:3",
                "image": file.relative_to(ROOT).as_posix(),
            }
        )
    items.sort(key=lambda i: (i["month"], i["variant"], i["id"]))
    return items


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    data = {
        "title": "Gen AI Calendar 2025",
        "slug": "aical2025",
        "items": build_items(),
    }
    out_path = DATA_DIR / "calendars.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=True, indent=2)


if __name__ == "__main__":
    main()
