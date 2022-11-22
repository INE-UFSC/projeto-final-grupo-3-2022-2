import pickle

"""
Pensei que seria melhor o dicionario ter a chave level e uma lista de tuplas (nickname, time) ordenados pelo time,
assim cada level teria uma lista com oito melhores scores que seriam mostrados durante o pause do level e
na escolha do level seria mostrado sempre a primeira tupla de cada level, que seria o melhor tempo dos leveis
"""

class ScoreDAO():
    def __init__(self, datasource = 'scores.pkl'):
        self.__datasource = datasource
        self.__objectCache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__objectCache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__objectCache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, level: int, nickname: str, time: float):
        if level in self.__objectCache: # Verifica se o level ja foi adicionado
            if len(self.__objectCache[level]) == 8: # Verifica se o tamanho da lista do level é igual a oito (limite de scores por level)
                self.__remove(level) # Remove o pior score (ultimo da lista ordenada pelo tempo)
            self.__objectCache[level].append((nickname, time)) # Adiciona os dados na lista
        else:
            self.__objectCache[level] = [(nickname, time)] # Se não, adiciona uma lista com a tupla com o dados

        self.__ordena(level) # Ordena a lista do level pelo tempo
        self.__dump()

    def __remove(self, level: int):
        self.__objectCache[level].pop(-1)

    def __ordena(self, level: int):
        for i in range(0, len(self.__objectCache[level])):
            for j in range(0, len(self.__objectCache[level])):
                if self.__objectCache[level][i][1] < self.__objectCache[level][j][1]:
                    temp = self.__objectCache[level][i]
                    self.__objectCache[level][i] = self.__objectCache[level][j]
                    self.__objectCache[level][j] = temp


    def get_level(self, level: int):
        return self.__objectCache[level]

    def get_all(self):
        return self.__objectCache