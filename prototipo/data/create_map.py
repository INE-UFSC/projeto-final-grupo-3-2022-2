from daos.LevelDAO import LevelDAO
from utility.finder import find_file

level_DAO = LevelDAO(find_file('default-levels.json'))

teste = {
    'level_name': 'Collision testing',
    'arrows': ['standart', 'bounce', 'fast', 'piercing'],
    'tile_map': ['                         ',
                 '                         ',
                 '                         ',
                 '                         ',
                 '                         ',
                 '     X             X     ',
                 '    X               X    ',
                 '    X      X    O   X    ',
                 '     X             X     ',
                 ' XX         P        DXX ',
                 'XXXXXXXXXXXXXXXXXXXXXXXXX']
}

level_DAO.add_level(teste)