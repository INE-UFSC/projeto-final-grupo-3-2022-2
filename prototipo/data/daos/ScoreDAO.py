from abstractDAO import AbstractDAO

class ScoreDAO(AbstractDAO):
    def __init__(self, datasource='scores.json'):
        super().__init__(datasource=datasource)

    def add(self, level: int, nickname: str, time: float):
        level = str(level)
        if level in self._objectCache:  # Verifica se o level ja foi adicionado
            # Verifica se o nickname ja foi adicionado
            if nickname in self._objectCache[level]:
                # Se o tempo for menor que o registrado armazena o novo tempo
                if time < self._objectCache[level][nickname]:
                    self._objectCache[level][nickname] = time
            else:
                # Se não tiver o nome e tiver 50 nomes
                if len(self._objectCache[level]) == 50:
                    # Verifica se o tempo é menor do que o maior tempo do level
                    if time < max(self._objectCache[level].values()):
                        nickname_toremove = sorted(
                            self._objectCache[level], key=self._objectCache[level].get)[-1]
                        # Remove o nickname com o menor tempo
                        self._objectCache[level].pop(nickname_toremove)
                        self._objectCache[level][nickname] = time
                else:
                    self._objectCache[level][nickname] = time
        else:
            # Se não, adiciona uma lista com a tupla com o dados
            self._objectCache[level] = {nickname: time}

        self._dump()

    def get_level(self, level: int):
        level = str(level)
        return self._objectCache[level]

    def get_all(self):
        return self._objectCache