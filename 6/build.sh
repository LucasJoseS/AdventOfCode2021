#!/usr/bin/sh

set -e

echo "Sample input"
go run -v lanternfish.go sample.input

echo "Input"
go run -v lanternfish.go input.input
