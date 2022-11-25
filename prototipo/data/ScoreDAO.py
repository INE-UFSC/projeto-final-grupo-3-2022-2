import abstractDAO


class ScoreDAO(abstractDAO):
    def __init__(self, datasource='scores.json'):
        super().__init__(datasource=datasource)

    def add(self, level: int, nickname: str, time: float):
        level = str(level)
        if level in self.__objectCache:  # Verifica se o level ja foi adicionado
            # Verifica se o nickname ja foi adicionado
            if nickname in self.__objectCache[level]:
                # Se o tempo for menor que o registrado armazena o novo tempo
                if time < self.__objectCache[level][nickname]:
                    self.__objectCache[level][nickname] = time
            else:
                # Se não tiver o nome e tiver 50 nomes
                if len(self.__objectCache[level]) == 50:
                    # Verifica se o tempo é menor do que o maior tempo do level
                    if time < max(self.__objectCache[level].values()):
                        nickname_toremove = sorted(
                            self.__objectCache[level], key=self.__objectCache[level].get)[-1]
                        # Remove o nickname com o menor tempo
                        self.__objectCache[level].pop(nickname_toremove)
                        self.__objectCache[level][nickname] = time
                else:
                    self.__objectCache[level][nickname] = time
        else:
            # Se não, adiciona uma lista com a tupla com o dados
            self.__objectCache[level] = {nickname: time}

        self.__dump()

    def get_level(self, level: int):
        level = str(level)
        return self.__objectCache[level]

    def get_all(self):
        return self.__objectCache
