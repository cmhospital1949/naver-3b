import os
import tempfile
import unittest

from chatbot import generate_reply

class DummyTokenizer:
    def decode(self, tokens, skip_special_tokens=True):
        return "dummy"

class DummyProcessor:
    def __call__(self, text=None, images=None, return_tensors=None):
        return {}

class DummyModel:
    def generate(self, **kwargs):
        return [[1, 2, 3]]

class GenerateReplyTest(unittest.TestCase):
    def test_image_optional(self):
        try:
            from PIL import Image
        except ImportError:
            self.skipTest("Pillow not installed")
        tmpdir = tempfile.gettempdir()
        img_path = os.path.join(tmpdir, "dummy.png")
        Image.new("RGB", (1, 1), color="white").save(img_path)
        reply = generate_reply(DummyTokenizer(), DummyProcessor(), DummyModel(), "hi", img_path)
        self.assertEqual(reply, "dummy")

if __name__ == "__main__":
    unittest.main()
