from abstractDAO import abstractDAO
from utility.classTileMapUtility import TileMapConverter
from NivelJaExisteException import NivelJaExisteException
from NivelNaoExisteException import NivelNaoExisteException


class LevelDAO(abstractDAO):

    def __init__(self, datasource='levels.json'):
        super().__init__(datasource=datasource)

    def get_levels_names(self):
        return self.__objectCache.keys()

    def get_level(self, name: str):
        return self.__objectCache[name]

    def add_level(self, level: dict):
        if level['level_name'] in self.__objectCache.keys():
            raise NivelJaExisteException(
                f"Nível com o nome {level['level_name']} já existe.")
        self.__objectCache[level['level_name']] = level
        self.__objectCache[level['level_name']['textures']
                           ] = TileMapConverter.convert(level['tile_map'])
        self.__dump()

    def remove_level(self, level_name: str):
        if level_name not in self.__objectCache.keys():
            raise NivelNaoExisteException(
                f"Nível com o nome {level_name} não existe.")
        del self.__objectCache[level_name]


if __name__ == '__main__':
    dao = LevelDAO()

    level = {
        'level_number': 1,
        'level_name': 'Level 1',
        'tile_map': [
            'XXXXXXXXXXXXXXXXXXXXXXXXX',
            'X                X      X',
            'X        O       X      X',
            'XXXX             X   O  X',
            'X                X      X',
            'X        XX      X      X',
            'X        X              X',
            'X        X              X',
            'X        X              X',
            'X   P    X      AAA  D  X',
            'XXXXXXXXXXXXXXXXXXXXXXXXX']
    }
