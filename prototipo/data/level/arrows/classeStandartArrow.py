from singletons.singletonAssets import Assets
from level.arrows.abstractArrow import Arrow


class StandartArrow(Arrow):
    def __init__(self):
        IMAGE = Assets().level_images['arrows']['standart']
        ICON_IMAGE = Assets().interface['arrows']['standart']

        super().__init__(10, 15, 0.2, IMAGE, ICON_IMAGE)
 