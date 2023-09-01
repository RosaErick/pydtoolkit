import unittest
from src.filesystem_analysis.fat_reader import FATReader

class TestFATReader(unittest.TestCase):

    def test_list_directory(self):
        fat_reader = FATReader("path/to/fat/image")
        fat_reader.list_directory("/")  # Here you'd actually check expected outcomes


    def test_get_file_metadata(self):
        fat_reader = FATReader("path/to/fat/image")
        metadata = fat_reader.get_file_metadata("/some_file.txt")
        # Add assertions to check the metadata is as expected


if __name__ == "__main__":
    unittest.main()
