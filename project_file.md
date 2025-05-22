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

## 3. Improvements
- Added CPU float32 loading and torch.no_grad wrapper.
- Added unit test verifying image handling in `generate_reply`.
