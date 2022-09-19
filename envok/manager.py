from .shared.utils import get_json

class EnvManager:
    def __init__(self, env_path: str) -> None:
        self.path = env_path

    def get_env(self, env: str) -> dict:
        """Return the requested env parameters"""
        envs = get_json(self.path)
        return envs[env]

    def save_env(config: dict) -> dict:
        """Save new env parameters"""
        pass

    def rm_env(env: str) -> bool:
        pass

    def update(env: str, config: dict) -> dict:
        pass

