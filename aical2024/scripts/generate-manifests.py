#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = ROOT / "images"
DATA_DIR = ROOT / "data"
PATTERN = re.compile(r"^cal2024-(\d{1,2})([a-z])\.jpg$")


def build_items() -> list[dict]:
    items = []
    for file in sorted(IMAGES_DIR.iterdir()):
        if not file.is_file():
            continue
        match = PATTERN.match(file.name)
        if not match:
            continue
        month_raw, variant_letter = match.groups()
        month_num = int(month_raw)
        month = f"2024-{month_num:02d}"
        variant = ord(variant_letter.lower()) - ord("a") + 1
        items.append(
            {
                "id": file.stem,
                "month": month,
                "brand": "aical",
                "variant": variant,
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
        "title": "AICAL 2024",
        "slug": "aical2024",
        "items": build_items(),
    }
    out_path = DATA_DIR / "calendars.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=True, indent=2)


if __name__ == "__main__":
    main()
