from .shared.utils import get_json, write_json

class EnvManager:
    def __init__(self, env_path: str) -> None:
        self.path = env_path

    def get_env(self, env: str) -> dict:
        """Return the requested env parameters"""
        envs = get_json(self.path)
        return envs[env]

    def save_env(self, env: str, config: dict) -> dict:
        """Save new env parameters"""
        envs = get_json(self.path)
        if env in envs:
            return envs
        else:
            envs[env] = config
            write_json(self.path, envs)
            envs = get_json(self.path)
            return envs

    def rm_env(env: str) -> bool:
        pass

    def update(env: str, config: dict) -> dict:
        pass

