from singletons.singletonAssets import Assets
from level.arrows.abstractArrow import Arrow


class FastArrow(Arrow):
    def __init__(self):
        MINIMUN_SPEED = 20
        IMAGE = Assets().level_images['arrows']['fast']
        ICON_IMAGE = Assets().interface['arrows']['fast']

        super().__init__(MINIMUN_SPEED, 5, 0.2, IMAGE, ICON_IMAGE)