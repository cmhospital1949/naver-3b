import os
import tempfile
import unittest

try:
    from PIL import Image
except Exception:
    Image = None

from main import generate_reply

class DummyProcessor:
    def __call__(self, text=None, images=None, return_tensors=None):
        self.text = text
        self.images = images
        self.return_tensors = return_tensors
        return {}

class DummyModel:
    def generate(self, **inputs):
        self.inputs = inputs
        return [[0]]

class DummyTokenizer:
    def decode(self, tokens, skip_special_tokens=True):
        self.tokens = tokens
        return "ok"

@unittest.skipIf(Image is None, "Pillow not installed")
class ImageReplyTest(unittest.TestCase):
    def test_generate_with_image(self):
        img = Image.new("RGB", (4, 4), color="white")
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            img.save(tmp.name)
            path = tmp.name

        tok = DummyTokenizer()
        proc = DummyProcessor()
        model = DummyModel()

        reply = generate_reply(tok, proc, model, "hi", path)
        self.assertEqual(reply, "ok")
        self.assertEqual(proc.text, ["hi"])
        self.assertEqual(len(proc.images), 1)
        self.assertIsInstance(proc.images[0], Image.Image)

        os.remove(path)

if __name__ == "__main__":
    unittest.main()
