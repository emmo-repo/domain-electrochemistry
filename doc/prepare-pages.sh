#!/bin/sh
# Bash script for generating and preparing documentation for GitHub Pages
set -ex

# Directories
rootdir=$(git rev-parse --show-toplevel)
ontodocdir=${rootdir}/${ONTODOC_DIR}
builddir=${ontodocdir}/${BUILD_DIR}
publishdir=${ontodocdir}/${PUBLISH_DIR}

# Generate documentation
${ontodocdir}/mkdoc.sh

# Copy documentation to publish dir
mkdir -p ${publishdir}
cp -ur ${builddir}/* ${publishdir}
mv ${publishdir}/electrochemistry.html ${publishdir}/index.html
