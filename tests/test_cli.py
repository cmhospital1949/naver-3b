import unittest
from main import build_parser

class ParserTest(unittest.TestCase):
    def test_defaults(self):
        parser = build_parser()
        args = parser.parse_args([])
        self.assertIsNone(args.image)
        self.assertFalse(args.gui)

if __name__ == '__main__':
    unittest.main()
