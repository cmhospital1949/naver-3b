# Project Plan

This document tracks development of the HyperCLOVAX chatbot example.

## 1. Setup Repository
- Add minimal `requirements.txt`.
- Create CLI and GUI in `main.py`.
- Ensure model loads in `float32`.

## 2. Improvements
- Wrapped generation in `torch.no_grad` and enforced CPU float32 loading.
- Added unit test for image handling (skipped if Pillow unavailable).


## 2. Added Features
- Implemented CLI conversation with optional image input.
- Implemented Tkinter GUI resembling WhatsApp style.
- Added basic unit test for CLI parser.
- Wrote README with usage instructions.
