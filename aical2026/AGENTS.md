# Repository Guidelines

This repository is a lightweight asset store for the AICAL 2026 site. It primarily contains static images and does not include application code or build tooling.

## Project Structure & Module Organization

- `images/` holds all image assets.
- `images/kageng/`, `images/nbp/`, `images/ice/` are subfolders grouped by source or partner.
- There are no source, test, or build directories in this repo today.

## Build, Test, and Development Commands

Manifest generation is handled via a small script:
- `python3 scripts/generate-manifests.py` regenerates `data/*.json` from `images/*` folders.
- `make manifests` runs the same manifest regeneration via `Makefile`.
- `make clean` removes all generated manifests in `data/*.json`.

## Coding Style & Naming Conventions

- Use lowercase directory and file names to match existing asset folders.
- Prefer short, descriptive names (e.g., `logo-header.png`, `banner-2026.jpg`).
- Keep non-asset files at the repository root when they are project-wide docs (e.g., `AGENTS.md`).

## Testing Guidelines

No automated tests are present. If you introduce tests, include:
- The framework used (e.g., Jest, pytest).
- The test file naming pattern (e.g., `*.spec.js`).
- How to run tests locally.

## Commit & Pull Request Guidelines

- Commit messages are short, imperative, and descriptive; recent history includes both English and Korean (e.g., `달력 페이지 추가.`).
- Keep PRs focused on a single change set and include a brief description of what assets were added or updated.
- For visual updates, attach a before/after screenshot or link to the rendered page where the asset is used.

## Asset Management Tips

- Group new assets into a sensible subfolder under `images/`.
- Avoid committing temporary files (like `.DS_Store`) when possible.
- Validate file sizes and formats to keep the repository lean.
