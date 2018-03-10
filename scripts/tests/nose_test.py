def multiply(a, b):
    """unit to test"""

    return a*b


class TestNose:

    def setup(self):
        print("TestUM:setup() before each test method")

    def teardown(self):
        print("TestUM:teardown() after each test method")

    def test_numbers_5_6_test(self):
        print('test_numbers_5_6()  <============================ actual test code')
        assert multiply(5, 6) == 30

    def test_strings_b_2_test(self):
        print('test_strings_b_2()  <============================ actual test code')
        assert multiply('b', 2) == 'bb'