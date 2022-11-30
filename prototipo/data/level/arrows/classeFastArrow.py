from singletons.singletonAssets import Assets
from level.arrows.abstractArrow import Arrow


class FastArrow(Arrow):
    def __init__(self):
        super().__init__(minimun_speed = 7,
                         maximun_extra_speed = 8)