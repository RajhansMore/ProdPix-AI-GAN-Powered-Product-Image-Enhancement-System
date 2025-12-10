#!/usr/bin/env bash
# create_venv.sh — create a Python virtual environment and install requirements
# Usage:
#   ./create_venv.sh         # creates .venv and installs packages from requirements.txt
#   ./create_venv.sh --no-install  # only create the venv, don't install requirements

set -euo pipefail

VENV_DIR=".venv"
PYTHON_CMD="${PYTHON:-python3}"
INSTALL=true

if [[ "${1:-}" == "--no-install" ]]; then
  INSTALL=false
fi

if ! command -v "$PYTHON_CMD" >/dev/null 2>&1; then
  echo "Error: $PYTHON_CMD not found. Install Python 3.8+ and try again."
  exit 1
fi

echo "Creating virtual environment in $VENV_DIR using $PYTHON_CMD..."
$PYTHON_CMD -m venv "$VENV_DIR"

echo "Upgrading pip in the venv..."
"$VENV_DIR/bin/pip" install --upgrade pip setuptools wheel

if [ "$INSTALL" = true ] ; then
  if [ -f "requirements.txt" ]; then
    echo "Installing packages from requirements.txt..."
    "$VENV_DIR/bin/pip" install -r requirements.txt
  else
    echo "No requirements.txt found — skipping package install."
  fi
else
  echo "Skipping installation of requirements (requested --no-install)."
fi

echo ""
echo "Virtual environment created at: $VENV_DIR"
echo "Activate it with:"
echo "  source $VENV_DIR/bin/activate    # bash / zsh"
echo "  source $VENV_DIR/bin/activate.fish # fish"
echo "  $VENV_DIR\\Scripts\\activate      # Windows (PowerShell/CMD via venv)"
echo ""
echo "To remove the venv: rm -rf $VENV_DIR"
