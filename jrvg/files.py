from pathlib import Path
import json
import yaml


def get_suffix(filename: str | Path) -> str:
    if isinstance(filename, str):
        return filename.split('.')[-1]
    return filename.suffix[1:]


def _load_json(file: str | Path):
    with open(file, 'rt') as f:
        return json.load(f)


def _load_yaml(file: str | Path):
    with open(file, 'rt') as f:
        return yaml.safe_load(f)


def _load_txt(file: str | Path):
    with open(file, 'rt') as f:
        return f.read()


def load(file: str | Path):
    suffix = get_suffix(file)
    match suffix:
        case 'json':
            _load_json(file)
        case 'yaml':
            _load_yaml(file)
        case 'txt':
            _load_txt(file)
        case other:
            raise ValueError(f'File extension `{other}` not supported')
