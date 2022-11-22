from ScoreDAO import ScoreDAO

class ScoreController():
    def __init__(self):
        self.__scoreDAO = ScoreDAO()

    def verify_time(self, level: int, time: int):
        if time > self.__scoreDAO.get_level(level)[-1] and len(self.__scoreDAO.get_level(level)) == 8:
            return False # O tempo não está entre os oitos melhores
        return True

    def add_score(self, level: int, nickname: str, time: float):
        self.__scoreDAO.add(level, nickname, time)

    def get_level_scores(self, level: int):
        return self.__scoreDAO.get_level(level)

    def get_all_scores(self):
        return self.__scoreDAO.get_all()