from abc import ABC
import json
class AbstractDAO(ABC):
    def __init__(self, datasource = ''):
        self.datasource = datasource
        self._objectCache = {}
        try:
            self._load()
        except FileNotFoundError:
            self._dump()

    def _dump(self):
        json.dump(self._objectCache, open(self.datasource, 'w'))

    def _load(self):
        self._objectCache = json.load(open(self.datasource, 'r'))