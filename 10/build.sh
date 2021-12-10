#!/usr/bin/sh

set -e

echo "Sample input"
python syntax_scoring.py sample.input

echo "Input"
python syntax_scoring.py input.input
