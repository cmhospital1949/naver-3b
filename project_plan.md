# Project Plan

This document tracks development of the HyperCLOVAX chatbot example.

## 1. Setup Repository
- Add minimal `requirements.txt`.
- Create CLI and GUI in `main.py`.
- Ensure model loads in `float32`.


## 2. Added Features
- Implemented CLI conversation with optional image input.
- Implemented Tkinter GUI resembling WhatsApp style.
- Added basic unit test for CLI parser.
- Wrote README with usage instructions.

## 3. Maintenance
- Consolidated notes from `project_file.md` into this file.
- Removed `project_file.md` from the repository.

## 4. Refactor
- Moved model utilities to new `chatbot.py` module.
- Updated `main.py` to import from `chatbot.py`.
- Adjusted tests to import the new module.

