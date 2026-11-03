#!/usr/bin/env bash
# Pull a Figma node as a PNG plus its layer structure, using the REST API.
#
# Why this exists: the Figma MCP server requires an EDITOR seat on the team
# that owns the file. The REST API only needs VIEW access, so this works on
# files the MCP refuses.
#
#   1. Make a token:  figma.com -> your avatar -> Settings -> Security
#                     -> Personal access tokens -> Generate new token
#                     Scopes needed: "File content" (read).
#   2. Save it:       echo 'figd_xxxxxxxx' > ~/.figma-token && chmod 600 ~/.figma-token
#   3. Run:           ./tools/figma-fetch.sh <file-key> <node-id> [scale]
#
#   e.g.  ./tools/figma-fetch.sh 8LqFO4NjyttqYMYpracfd0 140:4615 2
set -euo pipefail

TOKEN_FILE="${FIGMA_TOKEN_FILE:-$HOME/.figma-token}"
TOKEN="${FIGMA_TOKEN:-}"
[ -z "$TOKEN" ] && [ -f "$TOKEN_FILE" ] && TOKEN="$(tr -d '[:space:]' < "$TOKEN_FILE")"
if [ -z "$TOKEN" ]; then
  echo "No token. Put one in $TOKEN_FILE or set FIGMA_TOKEN." >&2
  echo "figma.com -> Settings -> Security -> Personal access tokens" >&2
  exit 1
fi

KEY="${1:?usage: figma-fetch.sh <file-key> <node-id> [scale]}"
NODE="${2:?usage: figma-fetch.sh <file-key> <node-id> [scale]}"
NODE="${NODE//-/:}"                     # accept 140-4615 or 140:4615
SCALE="${3:-2}"
OUT="${FIGMA_OUT:-figma-out}"
mkdir -p "$OUT"
SAFE="${NODE//:/-}"

echo "file $KEY · node $NODE · scale ${SCALE}x"

# 1 · the rendered image
IMG_JSON=$(curl -s --max-time 60 -H "X-Figma-Token: $TOKEN" \
  "https://api.figma.com/v1/images/${KEY}?ids=${NODE}&format=png&scale=${SCALE}")
ERR=$(printf '%s' "$IMG_JSON" | python3 -c 'import sys,json; d=json.load(sys.stdin); print(d.get("err") or "")' 2>/dev/null || echo "bad response")
if [ -n "$ERR" ] && [ "$ERR" != "None" ]; then
  echo "  Figma said: $ERR" >&2
  printf '%s\n' "$IMG_JSON" | head -c 400 >&2; echo >&2
  exit 1
fi
URL=$(printf '%s' "$IMG_JSON" | python3 -c 'import sys,json; print(json.load(sys.stdin)["images"].popitem()[1] or "")')
if [ -z "$URL" ] || [ "$URL" = "None" ]; then
  echo "  No image returned — is the node id right?" >&2; exit 1
fi
curl -sL --max-time 120 -o "$OUT/${SAFE}.png" "$URL"
echo "  png   -> $OUT/${SAFE}.png  ($(wc -c < "$OUT/${SAFE}.png" | tr -d ' ') bytes)"

# 2 · the layer tree, so names, text and structure are readable too
curl -s --max-time 60 -H "X-Figma-Token: $TOKEN" \
  "https://api.figma.com/v1/files/${KEY}/nodes?ids=${NODE}" > "$OUT/${SAFE}.json"
echo "  json  -> $OUT/${SAFE}.json  ($(wc -c < "$OUT/${SAFE}.json" | tr -d ' ') bytes)"

# 3 · a flat list of every text string in the design
python3 - "$OUT/${SAFE}.json" <<'PY' > "$OUT/${SAFE}-text.txt" 2>/dev/null || true
import sys, json
d = json.load(open(sys.argv[1]))
out = []
def walk(n, depth=0):
    if n.get('type') == 'TEXT' and n.get('characters'):
        out.append('%s%s' % ('  ' * depth, n['characters'].replace('\n', ' / ')))
    for c in n.get('children', []):
        walk(c, depth + 1)
for v in d.get('nodes', {}).values():
    walk(v.get('document', {}))
print('\n'.join(out))
PY
[ -s "$OUT/${SAFE}-text.txt" ] && echo "  text  -> $OUT/${SAFE}-text.txt  ($(wc -l < "$OUT/${SAFE}-text.txt" | tr -d ' ') strings)"
echo "done."
