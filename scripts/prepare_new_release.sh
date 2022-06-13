#!/bin/bash -v

new_v=$1
if [[ -z $1 ]]; then
    echo "Usage: $0 version"
    exit 1
fi

git reset
old_v=$(python3 -c 'from kong_pdk.const import __version__ as v; print("%.1f.%d" % (v, v*100%10))')
if [[ -z "$old_v" ]]; then
    echo "Unknown old version"
    exit 1
fi

echo "Creating new release $new_v from $old_v"
git branch -D release/${new_v}
git checkout -b release/${new_v}

new_v_py=$(python3 -c "print('$new_v'.split('.')[0] + '.'+''.join('$new_v'.split('.')[1:]))")
# file
sed -i "s/__version__ = '$old_v'/__version__ = '$new_v'/g" kong_pdk/const.py
git add -u

# changelog
git commit -m "release: $new_v"
git tag "$new_v"
git-chglog --output CHANGELOG.md
git add -u
git tag -d "$new_v"
git commit -m "release: $new_v"

