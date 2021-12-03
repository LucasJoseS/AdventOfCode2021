#/usr/bin/sh

set -e

echo "Simple input"
python binary_diagnostic.py simple.input

echo "Full input"
python binary_diagnostic.py full.input
