import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 3)  #помилка

if __name__ == "__main__":
    unittest.main()
