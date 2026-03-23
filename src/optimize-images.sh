#!/bin/bash

convert_image() {
    local img="$1"
    local ext="${img##*.}"
    local out="$img.webp"

    if [[ "$ext" =~ ^(gif|GIF)$ ]]; then
        # Use gif2webp for animations
        gif2webp -q 80 "$img" -o "$out" -quiet && rm "$img"
    else
        # Use cwebp for static images
        cwebp -q 80 "$img" -o "$out" -quiet && rm "$img"
    fi
}
export -f convert_image

# 1. Convert all images using 4 parallel workers (stable for CI)
find ./dist -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) | \
xargs -I {} -P 4 bash -c 'convert_image "$@"' _ {}

# 2. Update HTML references
# This regex targets local extensions and appends .webp 
# only if they aren't already converted.
echo "Updating HTML references..."
find ./dist -type f -name "*.html" | while read -r html; do
    sed -i -E 's/(\.(jpg|jpeg|png|gif))([^.]|$)/\1.webp\3/gI' "$html"
done