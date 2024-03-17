import unittest
from app.io.input import input_from_file, input_from_file_pandas


class TestInput(unittest.TestCase):
    def test_input_from_file(self):
        path = "D:/project_template/data/text.txt"
        expected_text = "This is test 1"
        with open(path, "w") as file:
            file.write(expected_text)
        actual_text = input_from_file(path)
        self.assertEqual(expected_text, actual_text)


test = TestInput()
test.test_input_from_file()

