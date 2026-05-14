# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A tiny Python script that reads `MOCK_DATA.csv` (generated mock user data) and prints full names to stdout.

## Commands

```bash
# Activate the virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Run the script
python display_names.py
```

No test runner, linter, or build system is configured.

## Architecture

- `display_names.py` — reads `MOCK_DATA.csv` via `csv.DictReader`, prints `first_name last_name` per row.
- `MOCK_DATA.csv` — ~1000 rows of mock data (id, first_name, last_name, email, gender, ip_address).
