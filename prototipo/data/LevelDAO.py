from abstractDAO import AbstractDAO
from utility.classTileMapUtility import TileMapConverter
from NivelJaExisteException import NivelJaExisteException
from NivelNaoExisteException import NivelNaoExisteException


class LevelDAO(AbstractDAO):

    def __init__(self, datasource='levels.json'):
        super().__init__(datasource)

    def get_levels_names(self):
        return self._objectCache.keys()

    def get_level(self, name: str):
        return self._objectCache[name]

    def add_level(self, level: dict):
        if level['level_name'] in self._objectCache.keys():
            raise NivelJaExisteException(
                f"Nível com o nome {level['level_name']} já existe.")
        self._objectCache[level['level_name']] = level
        self._objectCache[level['level_name']]['textures'] = TileMapConverter.convert(
            level['tile_map'])
        self._dump()

    def remove_level(self, level_name: str):
        if level_name not in self._objectCache.keys():
            raise NivelNaoExisteException(
                f"Nível com o nome {level_name} não existe.")
        del self._objectCache[level_name]


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
    level_2 = {
        'level_number': 2,
        'level_name': 'Level 2',
        'tile_map': [
            '                         ',
            '                         ',
            '                         ',
            '                         ',
            '                         ',
            '     X             X     ',
            '    X               X    ',
            '    X      X        X    ',
            '     X             X     ',
            ' XX         P         XX ',
            'XXXXXXXXXXXXXXXXXXXXXXXXX']
    }
    
    print(dao.get_levels_names())
    dao.add_level(level)
    dao.add_level(level_2)
    print(dao.get_levels_names())
