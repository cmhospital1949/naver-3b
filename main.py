import argparse

MODEL_NAME = "naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B"


def load_model():



    """Load tokenizer, processor, and model in float32 on CPU."""

    import torch
    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        AutoProcessor,
    )


    # Both the vision and language components must run in float32

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    processor = AutoProcessor.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float32,
        device_map="cpu",
    )
    model.eval()
    return tokenizer, processor, model


def generate_reply(tokenizer, processor, model, text, image_path=None):

  
    from PIL import Image
    image = Image.open(image_path).convert("RGB") if image_path else None
    inputs = processor(text=[text], images=[image] if image else None, return_tensors="pt")
    import torch
    with torch.no_grad():
        outputs = model.generate(**inputs)

    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reply


def chat_cli(args):
    tokenizer, processor, model = load_model()
    image_path = args.image
    while True:
        user = input("User: ")
        if user.strip().lower() == "quit":
            break
        reply = generate_reply(tokenizer, processor, model, user, image_path)
        print("Bot:", reply)
        image_path = None


def build_parser():
    parser = argparse.ArgumentParser(description="HyperCLOVAX Chatbot")
    parser.add_argument("--image", help="optional image path", default=None)
    parser.add_argument("--gui", action="store_true", help="launch GUI")
    return parser


def run_gui():
    import tkinter as tk
    from tkinter import filedialog, scrolledtext

    tokenizer, processor, model = load_model()
    window = tk.Tk()
    window.title("충무병원 전용 챗봇")

    chat_log = scrolledtext.ScrolledText(window, width=50, height=20)
    chat_log.pack()

    entry = tk.Entry(window, width=40)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    selected_image = {"path": None}

    def send():
        text = entry.get()
        if not text:
            return
        reply = generate_reply(tokenizer, processor, model, text, selected_image["path"])
        chat_log.insert(tk.END, f"You: {text}\n")
        if selected_image["path"]:
            chat_log.insert(tk.END, f"[Image: {selected_image['path']}]\n")
        chat_log.insert(tk.END, f"Bot: {reply}\n")
        entry.delete(0, tk.END)
        selected_image["path"] = None

    def attach_image():
        path = filedialog.askopenfilename(title="Select image")
        if path:
            selected_image["path"] = path
            chat_log.insert(tk.END, f"[Attached {path}]\n")

    send_btn = tk.Button(window, text="Send", command=send)
    send_btn.pack(side=tk.RIGHT)

    attach_btn = tk.Button(window, text="Attach Image", command=attach_image)
    attach_btn.pack(side=tk.RIGHT)

    window.mainloop()


def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.gui:
        run_gui()
    else:
        chat_cli(args)


if __name__ == "__main__":
    main()
