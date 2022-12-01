from singletons.singletonAssets import Assets
from level.arrows.abstractArrow import Arrow


class PiercingArrow(Arrow):
    def __init__(self):
        IMAGE = Assets().level_images['arrows']['piercing']

        super().__init__(10, 15, 0.2, IMAGE)
