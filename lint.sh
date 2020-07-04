#!/usr/bin/env bash

set -eu
set -o pipefail

cd "$(dirname "$0")" || exit


mypy --ignore-missing-imports -- *.py ./sortd/**.py

SCRIPTS=(
  sjson
  slines
  stoml
  syaml
)

for script in "${SCRIPTS[@]}"
do
  mypy --ignore-missing-imports -- "$script"
done
