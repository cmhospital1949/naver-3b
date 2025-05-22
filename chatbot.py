"""Core chatbot utilities for HyperCLOVAX example."""

MODEL_NAME = "naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B"


def load_model():
    """Load tokenizer, processor and model in float32 on CPU."""
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer, AutoProcessor
    except ImportError as exc:
        raise ImportError(
            "Required libraries not found. Install 'torch' and 'transformers'."
        ) from exc

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
    """Generate a reply to `text` optionally conditioned on an image."""
    from PIL import Image
    image = Image.open(image_path).convert("RGB") if image_path else None
    inputs = processor(text=[text], images=[image] if image else None, return_tensors="pt")
    import torch
    with torch.no_grad():
        outputs = model.generate(**inputs)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reply
