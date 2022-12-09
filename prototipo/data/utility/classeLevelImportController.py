from tkinter.filedialog import askopenfilename

from utility.staticTileMapUtility import TileMapUtility
from daos.LevelDAO import LevelDAO


class LevelImportController:
    def __init__(self, destination_json_name: str):
        self.__level_dao = LevelDAO(destination_json_name)
        self.__tile_map_utility = TileMapUtility()
        
    def import_from_file_picker(self):
        file_path = askopenfilename(filetypes=[("Map Files", ".ods")])
        try:
            tile_map = TileMapUtility.import_map_from_ods(file_path)
            self.__level_dao.add_level(tile_map)
        except Exception as e:
            raise e