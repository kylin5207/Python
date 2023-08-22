import unittest


class MyTestCase(unittest.TestCase):

    def test_method1(self):
        print(f"===test_method1===")
        # 这是你要运行的测试方法的代码
        assert 1==1, f"test_method1"

    def test_method2(self):
        print(f"===test_method2===")
        # 这是你要运行的测试方法的代码
        assert 2==2, f"test_method2"


if __name__ == '__main__':
    # all test play
    # unittest.main()

    # only one test
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_method2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)