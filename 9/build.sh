#!/usr/bin/sh

set -e
rustc smoke_basin.rs -o smoke_basin

echo "Sample input"
./smoke_basin sample.input

echo "Input"
./smoke_basin input.input
