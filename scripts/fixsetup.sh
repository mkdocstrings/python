#!/usr/bin/env bash
set -e

PYTHON_VERSIONS="${PYTHON_VERSIONS-3.7 3.8 3.9 3.10 3.11}"

for python_version in ${PYTHON_VERSIONS}; do
    rm -rf "__pypackages__/${python_version}/lib/mkdocstrings"
    rm -f "__pypackages__/${python_version}/lib/mkdocstrings.pth"
    cp -r ../mkdocstrings/src/mkdocstrings "__pypackages__/${python_version}/lib/"
    cp -r src/mkdocstrings/* "__pypackages__/${python_version}/lib/mkdocstrings"
done
