#!/usr/bin/sh
set -e

gcc -Wall hydrothermal_venture.c -o app

echo "Sample input"
./app sample.input

echo "Input"
./app input.input
