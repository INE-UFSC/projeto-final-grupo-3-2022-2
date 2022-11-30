import sys
sys.path.append("..")
from abstractDAO import AbstractDAO
from daos.exceptions.NivelJaExisteException import NivelJaExisteException
from daos.exceptions.NivelNaoExisteException import NivelNaoExisteException
from utility.staticLevelUtility import LevelUtility
class LevelDAO(AbstractDAO):

    def __init__(self, datasource='levels.json'):
        self.DEFAULT_LEVELS = ["Level 1", "Level 2", "Level 3"]
        super().__init__(datasource)
        try:
            level_1 = {
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
            # TODO Atualizar os níveis com as informações atualizadas posteriormente.
            self.add_level(level_1)
            self.add_level(level_2)
        except NivelJaExisteException:
            print("Erro já existe!")
        except:
            pass

    def get_levels_names(self):
        return self._objectCache.keys()

    def get_level(self, name: str):
        return self._objectCache[name]

    def add_level(self, level: dict):
        if level['level_name'] in self._objectCache.keys():
            raise NivelJaExisteException(
                f"Nível com o nome {level['level_name']} já existe.")
        self._objectCache[level['level_name']] = level
        self._objectCache[level['level_name']]['textures'] = LevelUtility.convert(
            level['tile_map'])
        self._dump()

    def remove_level(self, level_name: str):
        if level_name not in self._objectCache.keys():
            raise NivelNaoExisteException(
                f"Nível com o nome {level_name} não existe.")
        if level_name not in self.DEFAULT_LEVELS:
            del self._objectCache[level_name]