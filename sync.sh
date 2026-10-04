#!/usr/bin/env bash
# Pull the repo and print the standing brief's headlines plus what is open.
set -uo pipefail
cd "$(dirname "$0")"

echo "── pulling ─────────────────────────────────────────────"
git pull --ff-only origin main 2>&1 | sed 's/^/  /'
echo "  HEAD: $(git rev-parse --short HEAD)  $(git log -1 --format=%s)"
[ -z "$(git status --porcelain)" ] && echo "  tree: clean" || { echo "  tree: UNCOMMITTED —"; git status --porcelain | sed 's/^/    /'; }

echo
echo "── read CONTEXT.md before starting ─────────────────────"
grep -n '^## ' CONTEXT.md | sed 's/^/  /'

echo
echo "── open, waiting on Dhanesh ────────────────────────────"
awk '/^## 9 · Open/{f=1;next} /^## /{f=0} f' CONTEXT.md | grep -E '^[0-9]+\.' | sed 's/^/  /'

echo
echo "── live ────────────────────────────────────────────────"
printf '  case study   HTTP %s\n' "$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 https://dhanesh100.github.io/Case-study/)"
