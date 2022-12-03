from daos.abstractDAO import AbstractDAO
from daos.exceptions.NivelJaExisteException import NivelJaExisteException
from daos.exceptions.NivelNaoExisteException import NivelNaoExisteException
from utility.staticLevelUtility import LevelUtility
from json import load

from utility.finder import find_file


# class LevelDAO(AbstractDAO):
#     def __init__(self, datasource):
#         super().__init__(cache=[], datasource=datasource)

#     def add_level(self, level_dict: dict):
#         # Confere o nome do nível no dicionário
#         if 'level_name' not in level_dict:
#             raise Exception("A chave 'level_name' contendo o nome do nível não foi encontrada no dicionário.")
#         elif level_dict['level_name'] == '' or isinstance(level_dict['level_name'], str) == False:
#             raise Exception("A chave 'level_name' contendo o nome do nível tem um valor vazio ou não é uma string.")
#         else:
#             for level in self._objectCache:
#                 if level['level_name'] == level_dict['level_name']:
#                     raise NivelJaExisteException(f"Level with name '{level_dict['level_name']}' already exists.")

#         # Tenta fazer a conversão do nível (a validação das informações específicas de criação de nível são conferidas)
#         try:
#             converted_dict = LevelUtility.convert(level_dict)
#         except Exception as e:
#             raise e

#         self._objectCache.append(converted_dict)
#         self._dump()

#     def remove_level(self, level_name: str):
#         for i, level in enumerate(self._objectCache, start = 0):
#             if level['level_name'] == level_name:
#                 self._objectCache.pop(i)
#                 return
#         raise NivelNaoExisteException(f"Level with name {level_name} doesn't exist.")


DEFAULT_LEVELS_PATH = find_file('default-maps.json')
CREATED_LEVELS_PATH = find_file('created-levels.json')


class LevelDAO(AbstractDAO):
    def __init__(self, datasource=find_file('default-maps.json')):
        super().__init__(datasource)
        self.__DEFAULT_OBJECTCACHE = load(open(DEFAULT_LEVELS_PATH, 'r'))

    # Default Levels
    def get_default_levels_names(self):
        return [x['level_name'] for x in self.__DEFAULT_OBJECTCACHE]

    def get_default_level(self, level_name):
        for i, level in enumerate(self.__DEFAULT_OBJECTCACHE, start=0):
            if level['level_name'] == level_name:
                return self.__DEFAULT_OBJECTCACHE[i]
        raise NivelNaoExisteException(
            f"Level with name {level_name} doesn't exist.")
    # End Default Levels

    # Custom Level
    def get_created_levels_names(self):
        return [x["level_name"] for x in self._objectCache]

    def get_created_level(self, level_name):
        for i, level in enumerate(self._objectCache, start=0):
            if level["level_name"] == level_name:
                return self._objectCache[i]
        raise NivelNaoExisteException(
            f"Level with name {level_name} doesn't exist.")

    def add_level(self, level_dict: dict):
        # Confere o nome do nível no dicionário
        if 'level_name' not in level_dict:
            raise Exception(
                "A chave 'level_name' contendo o nome do nível não foi encontrada no dicionário.")
        elif level_dict['level_name'] in self._objectCache.keys():
            raise NivelJaExisteException(
                f"Um nível com o nome {level_dict['level_name']} já existe.")

        # Tenta fazer a conversão do nível (a validação das informações específicas de criação de nível são conferidas)
        try:
            converted_dict = LevelUtility.convert(level_dict)
        except Exception as e:
            raise e

        self._objectCache.append(converted_dict)
        self._dump()

    def remove_level(self, level_name: str):
        for i, level in enumerate(self._objectCache, start=0):
            if level['level_name'] == level_name:
                self._objectCache.pop(i)
                return
        raise NivelNaoExisteException(
            f"Level with name {level_name} doesn't exist.")
