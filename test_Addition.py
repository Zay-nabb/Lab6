import unittest
from Addition import Addition
class TC(unittest.TestCase):
  def test_Add(self):
    res = Addition.add(1,1)
    self.assertEqual(res, 2)

if __name__ == "__main__":
    unittest.main()
