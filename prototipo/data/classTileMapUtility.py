from typing import List

class TileMapConverter():
    @staticmethod
    def convert(st: List[str]) -> List[str]:
        return_list = [[] for _ in range(len(st))]

        len_x = len(st[0])
        len_y = len(st)

        for x in range(len_x):
            for y in range(len_y):
                #Player = 1
                #Door = 2
                #Target = 3
                #Spike = 4
                #Upper Left = 11
                #Upper = 12
                #Upper Right = 13
                #Middle Left = 14
                #Middle = 15
                #Middle Right = 16
                #Down Left = 17
                #Down = 18
                #Down Right = 19

                if st[y][x] == "A":
                    return_list[y].append(4)
                elif st[y][x] == "P":
                    return_list[y].append(1)
                elif st[y][x] == "D":
                    return_list[y].append(2)
                else:
                    left = right = up = down = None
                    left_out = right_out = up_out = down_out = None

                    # verifica se left é um tile de parede
                    if x == 0:
                        left = False
                    else:
                        if st[y][x-1] == "X":
                            left = True

                    # verifica se right é um tile de parede
                    if x == len_x - 1:
                        right = False
                    else:
                        if st[y][x + 1] == "X":
                            right = True

                    # verifica se up é um tile de parede
                    if y == 0:
                        up = False
                    else:
                        if st[y - 1][x] == "X":
                            up = True

                    # verifica se down é um tile de parede
                    if y == len_y - 1:
                        down = False
                    else:
                        if st[y + 1][x] == "X":
                            down = True

                    if left and right and up and down:
                        pass

                    # if up

