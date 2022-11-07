from os import path
from prototipo.abstractArrow import Arrow

class StandartArrow(Arrow):
    def __init__(self, tipo: str = 'normal'):
        IMAGE_PATH = path.join('arrow.png')
        
        super().__init__(IMAGE_PATH, 10, 15, 0.2)
 