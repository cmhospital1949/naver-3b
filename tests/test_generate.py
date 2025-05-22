import os
import tempfile
import unittest
from unittest.mock import MagicMock
try:
    from PIL import Image
    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False

from main import generate_reply

class GenerateReplyImageTest(unittest.TestCase):
    @unittest.skipUnless(PIL_AVAILABLE, "Pillow not installed")
    def test_generate_with_image(self):
        tokenizer = MagicMock()
        processor = MagicMock()
        model = MagicMock()
        tokenizer.decode.return_value = "ok"
        processor.return_value = {"pixel_values": "dummy"}
        model.generate.return_value = [[1]]

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            Image.new("RGB", (1, 1)).save(tmp.name)
        try:
            reply = generate_reply(tokenizer, processor, model, "hi", tmp.name)
            self.assertEqual(reply, "ok")
            processor.assert_called()
            model.generate.assert_called()
        finally:
            os.unlink(tmp.name)

if __name__ == "__main__":
    unittest.main()
