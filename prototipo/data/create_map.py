from daos.LevelDAO import LevelDAO
from utility.finder import find_file

level_DAO = LevelDAO('default-levels.json')

teste = {
    'level_name': 'Using the knockback',
    'arrows': ['standart'],
    'tile_map': ['XXXXXXXXXXXXXXXXXXXXXXXXX',
                 'X                       X',
                 'X                       X',
                 'X                       X',
                 'X P                   D X',
                 'XXXXXXXXX       XXXXXXXXX',
                 'XXXXXXXXX       XXXXXXXXX',
                 'XXXXXXXXX   O   XXXXXXXXX',
                 'XXXXXXXXX       XXXXXXXXX',
                 'XXXXXXXXXAAAAAAAXXXXXXXXX',
                 'XXXXXXXXXXXXXXXXXXXXXXXXX']
}

level_DAO.add_level(teste)