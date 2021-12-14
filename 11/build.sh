#!/usr/bin/sh

set -e

gcc -Wall -o cute dumbo_octopus.c

echo "Sample input"
./cute sample.input

echo "Input input"
./cute input.input 
