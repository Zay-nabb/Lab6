import unittest
from Addition import Addition
class TC(unittest.TestCase):
  def test_Add(self):
    res = Addition.Add(1,1)
    self.assertEqual(res, 2)
    
    res = Addition.Add(-5,5)
    self.assertEqual(res, 0)
    
    res = Addition.Add(-7,-3)
    self.assertEqual(res, -10)

if __name__ == "__main__":
    unittest.main()
