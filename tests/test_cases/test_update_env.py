import os
import unittest
from envok import manager

class TestUpdateEnv(unittest.TestCase):
    def test_update_env(self):
        '''Test updating an environment configuration'''
        cwd = os.getcwd()
        path = os.path.join(cwd, 'tests/env.json')
        m = manager.EnvManager(path)
        env = m.update_env('dev', {
            'my_param': 'baz'
        })
        self.assertDictContainsSubset({
            'dev': {
                'account_id': '1223334444',
                'region': 'us-west-2',
                'my_param': 'baz'
            }
        }, env)

if __name__ == '__main__':
    unittest.main()