import unittest
import os

try:
    from PIL import Image
except ImportError:  # pragma: no cover - PIL may not be installed
    PIL = None
else:
    PIL = Image

from chatbot import generate_reply

class DummyTokenizer:
    def decode(self, outputs, skip_special_tokens=True):
        return "dummy"

class DummyProcessor:
    def __call__(self, text=None, images=None, return_tensors=None):
        # mimic processor returning dict of tensors
        return {}

class DummyModel:
    def generate(self, **kwargs):
        return [[0]]

class ImageTest(unittest.TestCase):
    def setUp(self):
        if not PIL:
            self.skipTest("Pillow not available")

    def test_generate_with_image(self):
        img = PIL.new("RGB", (1, 1), color="white")
        img_path = "test_img.png"
        img.save(img_path)
        try:
            reply = generate_reply(DummyTokenizer(), DummyProcessor(), DummyModel(), "hi", img_path)
            self.assertEqual(reply, "dummy")
        finally:
            os.remove(img_path)

if __name__ == '__main__':

    unittest.main()
