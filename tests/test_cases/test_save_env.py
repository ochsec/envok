import os
import unittest
from envok import manager

class TestSaveEnv(unittest.TestCase):
    def test_save_new(self):
        """Test saving a new env config"""
        cwd = os.getcwd()
        path = os.path.join(cwd, "tests/env.json")
        m = manager.EnvManager(path)
        env = m.save_env('tst', {
            'account_id': 'q1ww22eee333',
            'region': 'us-east-1'
        })
        self.assertDictEqual(env, {
            "dev": {
                "account_id": "1223334444",
                "region": "us-west-2",
                "my_param": "foobar"
            },
            "tst": {
                "account_id": "q1ww22eee333",
                "region": "us-east-1"         
            }
        })

    def test_save_existing(self):
        """Test saving an existing environment."""
        cwd = os.getcwd()
        path = os.path.join(cwd, "tests/env.json")
        m = manager.EnvManager(path)
        env = m.save_env('dev', {
            "account_id": "1223334444",
            "region": "us-west-2",
            "my_param": "foobar"            
        })
        self.assertDictContainsSubset({
            "dev": {
                "account_id": "1223334444",
                "region": "us-west-2",
                "my_param": "foobar"
            }
        }, env)

if __name__ == "__main__":
    unittest.main()