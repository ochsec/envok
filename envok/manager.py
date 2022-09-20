from .shared.utils import get_json, write_json
from pprint import pprint

class EnvManager:
    def __init__(self, env_path: str) -> None:
        self.path = env_path

    def get_env(self, env: str) -> dict:
        '''Return the requested env parameters'''
        envs = get_json(self.path)
        return envs[env]

    def save_env(self, env: str, config: dict) -> dict:
        '''Save new env parameters'''
        envs = get_json(self.path)
        if env in envs:
            return envs
        else:
            envs[env] = config
            write_json(self.path, envs)
            envs = get_json(self.path)
            return envs

    def rm_env(self, env: str) -> bool:
        '''Removes the environment corresponding to the key'''
        envs = get_json(self.path)
        if env in envs:
            del envs[env]
            write_json(self.path, envs)
            envs = get_json(self.path)
            return envs
        else:
            envs = get_json(self.path)
            return envs

    def update_env(self, env: str, config: dict) -> dict:
        '''Updates an environment configuration'''
        envs = get_json(self.path)
        pprint(envs)
        if env in envs:
            for k, v in config:
                print(f'{k}: {v}')
                env[k] = v
            print(envs)
            write_json(self.path, envs)
            envs = get_json(self.path)
            return envs
        else:
            envs = get_json(self.path)
            return envs
