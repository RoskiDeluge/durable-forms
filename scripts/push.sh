#!/usr/bin/env bash
# Bump the draft version by 0.01, commit the bump, and push.
# Every push to origin is one draft increment, so use this instead of `git push`.
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
  echo "Working tree has uncommitted changes; commit or stash them first." >&2
  exit 1
fi

git fetch -q origin
if [ -z "$(git rev-list origin/main..HEAD)" ]; then
  echo "Nothing to push; draft version unchanged." >&2
  exit 1
fi

old=$(sed -n 's/^description: .*draft \([0-9]*\.[0-9]*\)$/\1/p' docs/_config.yml)
if [ -z "$old" ]; then
  echo "Could not read the current draft version from docs/_config.yml." >&2
  exit 1
fi
new=$(awk -v v="$old" 'BEGIN { printf "%.2f", v + 0.01 }')
month=$(LC_ALL=C date +"%B %Y")

sed -i '' -E \
  -e "s/draft [0-9]+\.[0-9]+\$/draft $new/" \
  -e "s/draft [0-9]+\.[0-9]+, [A-Za-z]+ [0-9]{4}\./draft $new, $month./" \
  docs/_config.yml
sed -i '' -E "s/Draft [0-9]+\.[0-9]+ · [A-Za-z]+ [0-9]{4}/Draft $new · $month/" docs/index.md
sed -i '' -E "s/Draft [0-9]+\.[0-9]+ \([A-Za-z]+ [0-9]{4}\)/Draft $new ($month)/" README.md

git add docs/_config.yml docs/index.md README.md
git commit -q -m "Bump draft to $new"
git push "$@" origin HEAD:main
echo "Pushed draft $new ($month)."
