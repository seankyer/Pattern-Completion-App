import unittest

class SimpleTestTest(unittest.TestCase):

    def test_lin_int(self):
        self.assertEqual('foo', 'foo')
        # print('wussup')



if __name__ == '__main__':
    unittest.main()