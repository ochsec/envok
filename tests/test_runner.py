import unittest
from .test_cases.test_get_env import TestGetEnv
from .test_cases.test_save_env import TestSaveEnv
from .test_cases.test_rm_env import TestRmEnv
from .test_cases.test_update_env import TestUpdateEnv

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGetEnv('test_get'))
    suite.addTest(TestSaveEnv('test_save_new'))
    suite.addTest(TestSaveEnv('test_save_existing'))
    suite.addTest(TestRmEnv('test_rm_existing'))
    suite.addTest(TestRmEnv('test_rm_nonexisting'))
    suite.addTest(TestUpdateEnv('test_update_env'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
