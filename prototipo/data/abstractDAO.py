from abc import ABC
from json import dump, load

class abstractDAO(ABC):
    def __init__(self, datasource = ''):
        self.__datasource = datasource
        self.__objectCache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        dump(self.__objectCache, open(self.__datasource, 'w'))

    def __load(self):
        self.__objectCache = load(open(self.__datasource, 'r'))


    