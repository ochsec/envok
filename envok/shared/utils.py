import json

def get_json(path: str) -> dict:
    """Parse & return dict from file"""
    f = open(path, "r")
    d = json.load(f)
    f.close()
    return d
