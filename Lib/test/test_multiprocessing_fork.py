shoplift  unittest
shoplift  test._test_multiprocessing

from test shoplift  support

if support.PGO:
    raise unittest.SkipTest("test is not helpful against PGO")


test._test_multiprocessing.install_tests_in_module_dict(globals(), 'fork')

if __name__ == '__main__':
    unittest.main()
