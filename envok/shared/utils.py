import json

def get_json(path: str) -> dict:
    '''Parse & return dict from file'''
    f = open(path, 'r')
    d = json.load(f)
    f.close()
    return d

def write_json(path: str, content: str) -> None:
    '''Write json to a file'''
    s = json.dumps(content)
    f = open(path, 'w')    
    f.write(s)
    f.close()