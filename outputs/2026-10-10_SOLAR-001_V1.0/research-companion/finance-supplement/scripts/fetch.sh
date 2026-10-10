#!/bin/zsh
# Usage: fetch.sh <subdir> <source_id> <url> <local_file>
# Saves a public file unchanged under Data/raw/2026-10-09_Finance-Deepening/<subdir>/ and appends a receipt row.
set -u
ROOT=/Users/duanlian/Desktop/OPT-Self-Employment/03-Work-Evidence/Projects/2026-08-SOLAR-001-AI-Power-Solar-Economics/Data/raw/2026-10-09_Finance-Deepening
D=$ROOT/$1; mkdir -p $D; R=$D/fetch_receipts.csv
[[ -f $R ]] || echo "source_id,url,local_file,retrieved_utc,http_status,content_type,sha256,bytes" > $R
out=$(curl -sL --max-time 120 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36" -o "$D/$4" -w "%{http_code},%{content_type}" "$3")
echo "$2,\"$3\",$4,$(date -u +%FT%TZ),$out,$(shasum -a 256 "$D/$4" | cut -d' ' -f1),$(stat -f%z "$D/$4")" >> $R
tail -1 $R
