#! /usr/bin/env bash

set -x


find . -type f -name "*.svg" -exec svg2pdf {} {}.pdf \;

