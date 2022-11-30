from singletons.singletonAssets import Assets
from level.arrows.abstractArrow import Arrow


class FastArrow(Arrow):
    def __init__(self):
        MINIMUN_SPEED = 20
        super().__init__(MINIMUN_SPEED, 5, 0.2)