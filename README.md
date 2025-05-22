# HyperCLOVAX Chatbot Example

This repository demonstrates a minimal chatbot built with
[naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B].
The bot supports text and image inputs and includes a simple GUI.
The model must be loaded in **float32** precision for both the language and
vision components due to the anyres projector.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

- **CLI**

```bash
python main.py --image path/to/image.jpg
```
Type messages and enter `quit` to exit.

- **GUI**

```bash
python main.py --gui
```

The window resembles a WhatsApp chat with the title **"충무병원 전용 챗봇"**.
Use the **Attach Image** button to send an image.

## Tests

Run the unit tests with:

```bash
python -m unittest discover -s tests -v
```

