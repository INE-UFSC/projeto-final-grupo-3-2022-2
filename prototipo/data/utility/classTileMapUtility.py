from typing import List


class TileMapConverter():
    @staticmethod
    def convert(st: List[str]) -> List[str]:
        return_list = [[] for _ in range(len(st))]

        for item in st:
            item.insert(0, "X")
            item.append("X")

        st.insert(0, ["X" for _ in range((len(st[0])))])
        st.append(["X" for _ in range((len(st[0])))])

        len_x = len(st[0])-1
        len_y = len(st)-1

        down = 1
        up = 2
        right = 4
        left = 8
        down_right = 16
        down_left = 32
        up_right = 64
        up_left = 128

        tiles = {
            21: "out_corner_up_left",
            61: "out_up",
            41: "out_corner_up_right",
            87: "out_left"
        }
        for x in range(1, len_x):
            for y in range(1, len_y):

                if st[y][x] == "A":
                    return_list[y].append(4)
                elif st[y][x] == "P":
                    return_list[y].append(1)
                elif st[y][x] == "D":
                    return_list[y].append(2)
                else:
                    total = 0

                    if st[y-1][x-1] == "X":
                        total += up_left
                    if st[y][x-1] == "X":
                        total += left
                    if st[y+1][x-1] == "X":
                        total += down_left
                    if st[y-1][x] == "X":
                        total += up
                    if st[y+1][x] == "X":
                        total += down
                    if st[y-1][x+1] == "X":
                        total += up_right
                    if st[y][x+1] == "X":
                        total += right
                    if st[y+1][x+1] == "X":
                        total += down_right
                    try:
                        return_list[y].append(tiles[total])
                    except KeyError:
                        print("Erro ao processar tilemap")
