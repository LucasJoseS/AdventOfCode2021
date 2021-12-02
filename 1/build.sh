#!/usr/bin/sh

set -e

echo "Simple input"
python measuring.py simple.input

echo "Full input"
python measuring.py full.input
