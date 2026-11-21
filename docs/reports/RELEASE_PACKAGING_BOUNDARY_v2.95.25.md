# Release packaging boundary fix — v2.95.25

## Finding
The packager excluded any directory component named `archive`, which unintentionally removed `docs/archive/PROJECT_HISTORY.md` from FullSource packages. It also did not explicitly exclude `.tmp` artifacts.

## Change
- Exclude only repository-root `archive/` as a directory.
- Preserve nested documentation history such as `docs/archive/`.
- Exclude `.tmp` files alongside `.zip`, `.bundle`, `.log`, and `.pyc`.
- Add package-source tests proving root archive/release/log/temp exclusions and nested documentation history inclusion.

## Validation
- `test_package_source.py`: 3/3 PASS.
- Package CRC, single-root and exclusion validation are performed after packaging.
- No app runtime, learner data, UI layout, or version markers changed.
