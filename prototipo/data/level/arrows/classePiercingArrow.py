from singletons.singletonAssets import Assets
from level.arrows.abstractArrow import Arrow


class PiercingArrow(Arrow):
    def __init__(self):
        super().__init__(minimun_speed = 5,
                         maximun_extra_speed = 2.5)
