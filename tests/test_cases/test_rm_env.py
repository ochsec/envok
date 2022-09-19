import os
import unittest
from envok import manager

class TestRmEnv(unittest.TestCase):
    def test_rm_existing(self):
        """Test removing an existing env config"""
        cwd = os.getcwd()
        path = os.path.join(cwd, "tests/env.json")
        m = manager.EnvManager(path)
        env = m.rm_env('tst')
        self.assertDictEqual(env, {
            "dev": {
                "account_id": "1223334444",
                "region": "us-west-2",
                "my_param": "foobar"
            }
        })

    def test_rm_nonexisting(self):
        """Test removing an environment that doesn't exist"""
        cwd = os.getcwd()
        path = os.path.join(cwd, "tests/env.json")
        m = manager.EnvManager(path)
        env = m.rm_env('prd')
        self.assertDictContainsSubset({
            "dev": {
                "account_id": "1223334444",
                "region": "us-west-2",
                "my_param": "foobar"
            }
        }, env)

if __name__ == "__main__":
    unittest.main()