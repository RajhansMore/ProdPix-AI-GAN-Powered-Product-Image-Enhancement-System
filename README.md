# ProdPix — AI / GAN Powered Product Image Enhancement

This repository contains the codebase for ProdPix, a GAN-based product image enhancement system.

Files added in this change:
- create_venv.sh — helper script to create a Python virtual environment and install requirements
- requirements.txt — initial dependency list
- .gitignore — ignore common venv and Python artifacts

## Prerequisites

- Python 3.8+
- git (optional)
- For GPU acceleration: install a CUDA-enabled PyTorch build from https://pytorch.org/

## Quick start

1. Create and bootstrap the virtual environment:
   Make the script executable (once):
   ```bash
   chmod +x create_venv.sh
   ```
   Then run:
   ```bash
   ./create_venv.sh
   ```
   This creates a `.venv` directory, upgrades pip, and installs packages from `requirements.txt`.

   If you prefer only to create the venv without installing packages:
   ```bash
   ./create_venv.sh --no-install
   ```

2. Activate the virtual environment:
   - macOS / Linux (bash / zsh):
     ```bash
     source .venv/bin/activate
     ```
   - fish:
     ```bash
     source .venv/bin/activate.fish
     ```
   - Windows (PowerShell):
     ```
     .venv\Scripts\Activate.ps1
     ```

3. Adjust PyTorch for your system if you need CUDA support:
   The `requirements.txt` includes `torch` as a placeholder. For GPU support, install torch using the official selector at:
   https://pytorch.org/get-started/locally/

## Recommendations

- Add `.venv/` to `.gitignore` (included here) to avoid committing environment files.
- Pin package versions in `requirements.txt` once the project's dependencies stabilise to ensure reproducible installs.

## Next steps I can take for you
- Push these files to the branch `setup/venv-and-docs`.
- Create a PR from that branch into your default branch.
- Pin package versions by scanning the repository for imports and suggesting appropriate versions.
