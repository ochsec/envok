import unittest
from .test_cases.test_get_env import TestGetEnv
from .test_cases.test_save_env import TestSaveEnv
from .test_cases.test_rm_env import TestRmEnv

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGetEnv('test_get'))
    suite.addTest(TestSaveEnv('test_save_new'))
    suite.addTest(TestSaveEnv('test_save_existing'))
    suite.addTest(TestRmEnv('test_rm_existing'))
    suite.addTest(TestRmEnv('test_rm_nonexisting'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
