import unittest
from src.filesystem_analysis.fat_reader import FATReader

class TestFATReader(unittest.TestCase):

    def test_list_directory(self):
        fat_reader = FATReader("path/to/fat/image")
        fat_reader.list_directory("/")  # Here you'd actually check expected outcomes

if __name__ == "__main__":
    unittest.main()
