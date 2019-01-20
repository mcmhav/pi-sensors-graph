import os
import yaml
from pathlib import Path


def get_yaml(config_path):
    """
    """
    path = Path(config_path)

    if path.is_file():
        path = os.path.join(config_path)
        f = open(path)
        s = yaml.load(f)
        f.close()

        return s.decode() if isinstance(s, bytes) else s
    else:
        raise ValueError('Could not find configfile at {}'.format(config_path))

    return None
