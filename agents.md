# HyperCLOVAX SEED Vision Instruct 3B Chatbot

This repository contains a simple example chatbot built on top of
[naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B).
The bot supports both text-only and multimodal (image + text) interactions.

> **Note**: The model requires loading in `float32` precision for both the
> language and vision components as mentioned in the official discussions.

## Getting Started

The minimal example below demonstrates how to start an interactive conversation:

```bash
pip install -r requirements.txt
python main.py --image path/to/image.jpg
python main.py --gui   # launch GUI
```

The CLI prompts for your messages. Enter `quit` to exit the session. The GUI
provides a WhatsApp-style window with an *Attach Image* button.

The `requirements.txt` file lists the minimal dependencies:

```
transformers
torch
Pillow
```

Please ensure the model loads in `float32` precision as required. The loader
handles this automatically. See `project_plan.md` for development notes.

## Running Tests

To run the unit tests:

```bash
python -m unittest discover -s tests -v
```

Using `python -m unittest` without the `discover` arguments may attempt to
import real dependencies and fail.