#!/bin/sh

tw() {
    echo "Building Tailwind CSS to dist/index.css"
    ./node_modules/.bin/tailwindcss -i ./src/index.css -o ./dist/index.css --minify
}

html() {
    echo "Building HTML files to dist"
    python src/build.py --output dist --no-clean
}

static() {
    for ent in public/*; do
        echo "Copying $ent to dist/${ent##*/}"
        cp -r "$ent" "dist/${ent##*/}"
    done
}

opt_imgs() {
    ./src/optimize-images.sh
}

# 1. Preparation
rm -rf dist && mkdir dist

# 2. Parallel Generation
tw &
html &
static &

# 3. Block and Wait
wait

# 4. Sequential Optimization
opt_imgs

echo "Build complete!"