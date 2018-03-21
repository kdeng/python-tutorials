#!/usr/bin/env bash

modules='bottle'

# Ignore test sources to be compressed
file_to_ignore='test'

# Create build directory
if [ -d dist ]; then
    rm -rf dist
fi

echo -e "\n[Build]: Creating dist directory"
mkdir -p dist

# Get needed libraries installed
if [ ! -f /app/dist/setup.cfg ]; then
    echo -e "[install]\nprefix=" >> /app/dist/setup.cfg
fi

# Move to work directory and install modules
cd /app/dist/
pip3 install --upgrade wheel
pip3 install --use-wheel ${modules} -t .
cd ..

# Copy all scripts
echo -e "\n[Build]: Copying all modules into /app/dist/ ..."
find ./src -maxdepth 1 ! -path ./src | egrep -v "${file_to_ignore}" | xargs -IELEMENT cp -r ELEMENT ./dist/

echo -e "\n[Build]: Done"