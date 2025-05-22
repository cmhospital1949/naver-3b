import unittest
import os

try:
    from PIL import Image
except ImportError:  # pragma: no cover - skip if Pillow missing
    PIL = None

from chatbot import generate_reply

class DummyTokenizer:
    def decode(self, outputs, skip_special_tokens=True):
        return "dummy"

class DummyProcessor:
    def __call__(self, text=None, images=None, return_tensors=None):
        # ensure an image was passed in
        if images is None:
            raise AssertionError("Image was not provided to processor")
        return {}

class ImagePathTest(unittest.TestCase):
    def setUp(self):
        if not PIL:
            self.skipTest("Pillow not available")
        self.img_path = "mock_img.png"
        PIL.new("RGB", (1, 1), color="white").save(self.img_path)

    def tearDown(self):
        if os.path.exists(self.img_path):
            os.remove(self.img_path)

    def test_generate_reply_uses_image_path(self):
        model = unittest.mock.MagicMock()
        model.generate.return_value = [[0]]

        reply = generate_reply(DummyTokenizer(), DummyProcessor(), model, "hi", self.img_path)
        self.assertEqual(reply, "dummy")
        model.generate.assert_called_once()

if __name__ == "__main__":
    unittest.main()
