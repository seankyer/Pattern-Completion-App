import unittest

# from main import generate
#      ^ if main is made into a package. Else:
# mainfile = __import__("../Main.py")
# generate = mainfile.generate
def generate(arr, length):
  if length == 0:
    return []
  elif arr == []:
    return False
  else:
    return []


# just testing the testing
def dummyFunction(x):
  return x + 1


class TestTester(unittest.TestCase):
  def test_tester(self):
    self.assertEqual(dummyFunction(10), 11)
    print("unittest is working!")


class TestEdgeCases(unittest.TestCase):
  def test_empty(self):
    arr = []
    self.assertEqual(generate(arr, 10), False)
  
  def test_length_zero(self):
    arr = ["not used lol"]
    self.assertEqual(generate(arr, 0), [])


class TestNumber(unittest.TestCase):
  def test_plus_one(self):
    arr = ["1", "2", "3"]
    self.assertEqual(generate(arr, 1), ["4"])
    self.assertEqual(generate(arr, 5), ["4", "5", "6", "7", "8"])

  def test_plus_two(self):
    arr = ["2", "4", "6"]
    self.assertEqual(generate(arr, 1), ["8"])
    self.assertEqual(generate(arr, 5), ["8", "10", "12", "14", "16"])

  def test_multiply_two(self):
    arr = ["2", "4", "8"]
    self.assertEqual(generate(arr, 1), ["16"])
    self.assertEqual(generate(arr, 5), ["16", "32", "64", "128", "256"])

class TestAlphabet(unittest.TestCase):
  def test_alphabet_basic(self):
    arr = ["a", "b" "c"]
    self.assertEqual(generate(arr, 1), ["d"])
    self.assertEqual(generate(arr, 5), ["d", "e", "f", "g", "h"])
  
  # Note that x is not a constant, it is part of the word
  def test_alphabet_offset(self):
    arr = ["xx", "xy" "xz", "ya"]
    self.assertEqual(generate(arr, 1), ["yb"])
    self.assertEqual(generate(arr, 5), ["yb", "yc", "yd", "ye", "yf"])


class TestText(unittest.TestCase):
  def test_constant(self):
    arr = ["123", "123", "123"]
    self.assertEqual(generate(arr, 2), ["123", "123"])
  
  def test_alternate(self):
    arr = ["a", "b", "a", "b"]
    self.assertEqual(generate(arr, 2), ["a", "b"])

  def test_concatenate(self):
    arr = ["-", "--", "---"]
    self.assertEqual(generate(arr, 2), ["----", "-----"])


class TestPatternComposition(unittest.TestCase):
  def test_repetition_numerical(self):
    arr = ["1", "1", "2", "2"]
    self.assertEqual(generate(arr, 4), ["3", "3", "4", "4"])

  def test_alphabet_concatenate(self):
    arr = ["a", "bb", "ccc", "dddd"]
    self.assertEqual(generate(arr, 2), ["eeeee", "ffffff"])
    
  def test_concatenate_alphabet(self):
    arr = ["a", "ab", "abc", "abcd"]
    self.assertEqual(generate(arr, 2), ["abcde", "abcdef"])


class TestPatternAddition2(unittest.TestCase):
  def test_constant_number(self):
    arr = ["row 1", "row 2", "row 3"]
    self.assertEqual(generate(arr, 2), ["row 4", "row 5"])

  def test_constant_alphabet(self):
    arr = ["row a", "row b", "row c"]
    self.assertEqual(generate(arr, 2), ["row d", "row e"])

  def test_alphabet_numerical(self):
    arr = ["a1", "b2", "c3"]
    self.assertEqual(generate(arr, 2), ["d4", "e5"])
    

if __name__ == '__main__':
    unittest.main()
