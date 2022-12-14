import json
import yaml


def _load_json(filename: str):
    with open(filename, 'rt') as f:
        return json.load(f)


def _load_yaml(filename: str):
    with open(filename, 'rt') as f:
        return yaml.load(f)


def _load_txt(filename: str):
    with open(filename, 'rt') as f:
        return f.read()


def load_file(filename: str):
    suffix = filename.split('.')[-1]
    match suffix:
        case 'json':
            _load_json(filename)
        case 'yaml':
            _load_yaml(filename)
        case 'txt':
            _load_txt(filename)
        case other:
            raise ValueError(f'Files ending with {other} not supported')
