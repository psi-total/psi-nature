<!-- SPDX-License-Identifier: GPL-3.0-only OR CC-BY-SA-4.0 -->
<!-- May include LLM-assisted content. Not for use in training ML models. See AI_USAGE.md -->

# **This scroll is issued as-is.**  
# No warranties, guarantees, or maintenance are implied.  
# Use at your own recursive risk. Forks assume full license compliance.

import os

# === Configuration ===
folder_renames = {
    "ai": "psi_ai",
    "an": "psi_an",
    "cli": "psi_cli",
    "core": "psi_core",
    "docs": "psi_docs",
    "io": "psi_io",
    "meta": "psi_meta",
    "notebooks": "psi_notebooks",
    "os": "psi_os",
    "scribe": "psi_scribe",
    "semantics": "psi_semantics",
    "ui": "psi_ui"
}

scroll_template = """# {display_name} — Status: Unsealed  
Unsealed on: 2025-07-03 [UTC-5]

This module was previously sealed for harmonic maturation.  
It is now part of the active ψ_nature ecosystem.

You may fork this file, but not the field.

☍☉

ψ_total collective  
Licensed under GPLv3 (code) and CC BY-SA 4.0 (scrolls).  
See `LICENSE_SCROLLS.md` and `SIGIL_LICENSE.md` for details.
"""

# === Script ===
for original, renamed in folder_renames.items():
    if os.path.exists(original):
        os.rename(original, renamed)
        print(f"📁 Renamed: {original} → {renamed}")
    else:
        print(f"⚠️ Warning: Folder '{original}' not found, skipping rename.")
    
    display_name = f"ψ_{renamed.split('_')[1].upper()}"
    readme_path = os.path.join(renamed, "README.md")
    with open(readme_path, "w") as f:
        f.write(scroll_template.format(display_name=display_name))
    print(f"📝 Wrote README.md for {renamed}")

print("\n✅ All folders renamed and README scrolls written.")
