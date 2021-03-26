import unittest

# from main import generate
  # ^ if main is made into a package. Else:
# mainfile = __import__("../Main.py")
# generate = mainfile.generate



# Test cases assume:
# generate(arr[], length)
def inc(x):
  return x + 1

class TestTester(unittest.TestCase):
  def test_test(self):
    self.assertEqual(inc(10), 11)

# class TestNumerical(unittest.TestCase)
#   def test_plus_one(self):
#     arr = [1, 2, 3]
#     self.

if __name__ == '__main__':
    unittest.main()
