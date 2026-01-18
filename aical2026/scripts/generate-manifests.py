#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = ROOT / "images"
DATA_DIR = ROOT / "data"
PATTERN = re.compile(r"^(\d{6})\+([A-Za-z0-9]+)\+(\d+)\+(43|169)\.jpg$")


def titleize(name: str) -> str:
    return name.upper() if name.islower() else name


def build_items(folder: Path) -> list[dict]:
    items = []
    for file in sorted(folder.iterdir()):
        if not file.is_file():
            continue
        match = PATTERN.match(file.name)
        if not match:
            continue
        yyyymm, brand, variant, ratio_code = match.groups()
        month = f"{yyyymm[:4]}-{yyyymm[4:]}"
        items.append(
            {
                "id": file.stem,
                "month": month,
                "brand": brand,
                "variant": int(variant),
                "ratio_code": ratio_code,
                "ratio": "4:3" if ratio_code == "43" else "16:9",
                "image": file.as_posix(),
            }
        )
    items.sort(key=lambda i: (i["month"], i["variant"], i["ratio_code"]))
    return items


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)

    existing = {p for p in DATA_DIR.glob("*.json")}
    generated = set()

    for folder in sorted(p for p in IMAGES_DIR.iterdir() if p.is_dir() and not p.name.startswith(".")):
        items = build_items(folder)
        data = {
            "title": titleize(folder.name),
            "slug": folder.name,
            "items": items,
        }
        out_path = DATA_DIR / f"{folder.name}.json"
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=True, indent=2)
        generated.add(out_path)

    for stale in existing - generated:
        stale.unlink()


if __name__ == "__main__":
    main()
