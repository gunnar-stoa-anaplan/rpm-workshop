#!/usr/bin/env bash
# ============================================================
# Anaplan Workshop — Canonical Design System Sync
#
# rpm-apps-workshop is the canonical home of:
#   css/style.css
#   js/nav.js
#   js/lab-quiz.js
#
# This script mirrors those three files from the rpm-apps-workshop
# working tree into the working trees of downstream workshop repos.
# Edit upstream (here), commit, then run this to push the bytes to
# the other repos for their own commit.
#
# Run from anywhere; the script resolves paths from its own location.
# Fails loudly on missing source files or unreachable targets.
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SRC_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

# Downstream workshop repos that consume the canonical design system.
# Add new workshops to this list as they come online.
TARGETS=(
  "$HOME/git-repos/ifp-delivery-workshop"
)

FILES=(
  "css/style.css"
  "js/nav.js"
  "js/lab-quiz.js"
)

echo "Canonical source: $SRC_ROOT"
echo

for target in "${TARGETS[@]}"; do
  if [[ ! -d "$target/.git" ]]; then
    echo "  SKIP: $target  (not a git repo)"
    continue
  fi
  echo "→ $target"
  for f in "${FILES[@]}"; do
    src="$SRC_ROOT/$f"
    dst="$target/$f"
    if [[ ! -f "$src" ]]; then
      echo "    MISSING source: $src" >&2
      exit 1
    fi
    mkdir -p "$(dirname "$dst")"
    cp "$src" "$dst"
    echo "    copied $f"
  done
done

echo
echo "Sync complete. Commit the changes in each target repo separately."
