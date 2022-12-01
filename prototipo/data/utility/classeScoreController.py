from daos.ScoreDAO import ScoreDAO

class ScoreController():
    def __init__(self):
        self.__scoreDAO = ScoreDAO()

    def add_score(self, level: int, nickname: str, time: float):
        self.__scoreDAO.add(level, nickname, time)

    def get_level_scores(self, level: int):
        scores = self.__scoreDAO.get_level(level)
        scores = self.__converte_tempo(sorted(scores.items(), key=lambda x:x[1]))
        return scores

    def get_all_scores(self):
        scores = {}
        for chave, valor in self.__scoreDAO.get_all().items():
            scores_level = self.__converte_tempo(sorted(valor.items(), key=lambda x:x[1]))
            scores[int(chave)] = scores_level
        
        return scores

    def __converte_tempo(self, scores_level: list):
        # Converte os floats com os segundos para uma string no formato min:seg.miliseg
        # Retorna uma lista de tuplas com os nomes dos jogadores e seus tempos convertidos

        formated_scores = []
        for name, time in scores_level:
            minutes, seconds = divmod(time, 60)
            formated_scores.append((name, "{:0>2}:{:05.2f}".format(int(minutes),seconds)))
        
        return formated_scores
