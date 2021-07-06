import os
import json
import logging.config
from pathlib import Path

import yaml

PROJECT_PATH = Path(__file__).parent.parent.resolve()


def configure_logger():
    with open(os.path.join(PROJECT_PATH, 'logging.yaml'), 'r') as f:
        log_cfg = yaml.safe_load(f.read())
        logging.config.dictConfig(log_cfg)


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls
                                        ).__call__(*args, **kwargs)
            return cls._instances[cls]


class Config(dict, metaclass=MetaSingleton):
    def __init__(self):
        dict.__init__(self, {})

    def _map_items(self, items: dict):
        for k, v in items.items():
            self.__setattr__(k.lower(), v)
            self[k] = v
        return True

    @staticmethod
    def _read_config(instance):
        config_path = os.path.join(PROJECT_PATH, 'instance', instance, 'config.json')
        with open(config_path, 'r') as f:
            return json.load(f)

    def from_json(self, instance='dev'):
        items = self._read_config(instance)
        self._map_items(items)

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, dict.__repr__(self))


config = Config()
config.from_json()
