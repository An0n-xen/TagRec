import unittest
import sys

sys.path.append("../Utils")
from Utils.utils import *


class TestFunctions(unittest.TestCase):
    def test_preprocess_text(self):
        text = "This is a sample text."
        expected_result = "sample text"
        result = preprocess_text(text)
        self.assertEqual(result, expected_result)

    def test_bag_of_words(self):
        processed_sentence = "sample text"
        all_patterns = ["sample", "text", "example"]
        all_patterns_dict = {"sample": 0, "text": 1, "example": 2}
        expected_result = [1.0, 1.0, 0.0]
        result = bag_of_words(processed_sentence, all_patterns, all_patterns_dict)
        self.assertEqual(result, expected_result)

    def test_generate_XY(self):
        data = [("sample1", "tag1"), ("sample2", "tag2")]
        all_patterns = ["sample1", "sample2"]
        expected_result_x = [[1.0, 0.0], [0.0, 1.0]]
        expected_result_y = ["tag1", "tag2"]
        result_x, result_y = generate_XY(data, all_patterns)
        self.assertEqual(result_x, expected_result_x)
        self.assertEqual(result_y, expected_result_y)


if __name__ == "__main__":
    unittest.main()
