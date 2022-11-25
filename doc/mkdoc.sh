#!/bin/sh
# Bash script for generating documentation
set -ex

# Directories
rootdir=$(git rev-parse --show-toplevel)
ontodocdir=${rootdir}/doc/ontodoc
tmpdir=${ontodocdir}/tmp

cd ${ontodocdir}

mkdir -p ${tmpdir}/figs
cp -u ${rootdir}/doc/img/bigmap.png ${tmpdir}/figs/.

ontograph -m ${rootdir}/electrochemistry.ttl ${tmpdir}/electrochemistry-structure.png
ontoconvert -si ${rootdir}/electrochemistry.ttl ${tmpdir}/electrochemistry-inferred.ttl

ontodoc --template=electrochemistry.md --format=html ${tmpdir}/electrochemistry-inferred.ttl \
        ${tmpdir}/electrochemistry.html

ontodoc --template=electrochemistry.md ${tmpdir}/electrochemistry-inferred.ttl \
        ${tmpdir}/electrochemistry.pdf
