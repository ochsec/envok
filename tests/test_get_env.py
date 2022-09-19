import os
import unittest
from envok import manager

class TestGetEnv(unittest.TestCase):
    def test_get(self):
        """
        Test getting a configuration from a json file
        """
        cwd = os.getcwd()
        path = os.path.join(cwd, "tests/env.json")
        m = manager.EnvManager(path)
        env = m.get_env('dev')
        self.assertDictEqual(
            env,
            {
                "account_id": "1223334444",
                "region": "us-west-2",
                "my_param": "foobar"
            })

if __name__ == "__main__":
    unittest.main()
