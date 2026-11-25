# Package Verification — v2.95.46

- Development base: user-supplied `TOEIC_Dictionary_v2.95.46_FullSource_Candidate(1).zip`.
- Base archive SHA-256: `4748288320b17ba4e94b1f5f064288034418ee23d1cc67a739d9614f9f410966`.
- Base inventory: 589 files; target clean source inventory: 485 files.
- Candidate-to-target delta: 7 additions, 13 modifications, 111 deletions. The 111 deletions are generated `.pyc` files under `__pycache__`; no application/data file was removed as part of this cleanup.
- Patch overlay: 20 files; deletion list: 111 paths.
- FullSource ZIP: one root folder, CRC PASS, clean extraction **485/485 byte-identical**.
- Exclusions verified: `__pycache__`, `.pyc`, logs, node_modules, nested ZIPs, bundles and temporary files are absent from FullSource.
- Candidate-based Patch: **REPLAY PASS** against the exact base archive above; all 589 base file hashes were checked, overlay/deletions applied, and all 485 target file hashes matched exactly.
- The Patch is not a v2.95.45-to-v2.95.46 official patch because the v2.95.45 ZIP was not supplied in this task.
- FullSource and Patch SHA-256 values are supplied in adjacent `.sha256` sidecars. The patch manifest stores the exact target tree fingerprint.
