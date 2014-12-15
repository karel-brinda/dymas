#! /usr/bin/env bash

#set -x
set -euf -o pipefail

cd cpp_progs/$1
cmake .
make
cp $1 ../..
cd ../..

