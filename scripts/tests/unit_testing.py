import unittest

def fun(x):
    return x + 2

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('setup')
        pass

    def test_upper(self):
        print('test1')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print('test2')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print('test3')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
if __name__ == '__main__':
    unittest.main()