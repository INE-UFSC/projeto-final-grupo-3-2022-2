from typing import List
import pylocalc as pl
from string import ascii_uppercase
# https://pypi.org/project/pylocalc/


class LevelUtility:
    @staticmethod
    def convert(tile_map: List[str]) -> List[str]:
        """Convert a list of tiles into a list of textures."""
        st = tile_map.copy()
        st.insert(0, ["X" for _ in range((len(st[0])))])
        st.append(["X" for _ in range((len(st[0])))])

        return_list = [[] for _ in range(len(st) - 2)]

        for i in range(len(st)):
            item = list(st[i])
            item.insert(0, "X")
            item.append("X")
            st[i] = item

        for x in range(1, len(st[0]) - 1):
            for y in range(1, len(st) - 1):
                context = {
                    "up_left": False,
                    "up": False,
                    "up_right": False,
                    "left": False,
                    "right": False,
                    "down_left": False,
                    "down": False,
                    "down_right": False,
                }
                if st[y][x] == " ":
                    return_list[y - 1].append(" ")
                elif st[y][x] == "A":
                    return_list[y - 1].append("A")
                elif st[y][x] == "P":
                    return_list[y - 1].append("P")
                elif st[y][x] == "D":
                    return_list[y - 1].append("D")
                elif st[y][x] == "O":
                    return_list[y - 1].append(" O ")
                elif st[y][x] == "X":
                    if st[y - 1][x - 1] == "X":
                        context["up_left"] = True
                    if st[y][x - 1] == "X":
                        context["left"] = True
                    if st[y + 1][x - 1] == "X":
                        context["down_left"] = True
                    if st[y - 1][x] == "X":
                        context["up"] = True
                    if st[y + 1][x] == "X":
                        context["down"] = True
                    if st[y - 1][x + 1] == "X":
                        context["up_right"] = True
                    if st[y][x + 1] == "X":
                        context["right"] = True
                    if st[y + 1][x + 1] == "X":
                        context["down_right"] = True
                    return_list[y - 1].append(
                        "B_" + str(LevelUtility.__get_tile(context))
                    )
                else:
                    return_list[y - 1].append("FAILED")
        return return_list

    @staticmethod
    def __get_tile(c: dict) -> int:
        if (c["up"] and c["right"] and c["left"] and c["down"]
                and c["up_left"] and c["up_right"] and c["down_left"] and c["down_right"]):
            return "black"  # black?
        elif (c["left"] and c["up"] and c["right"] and c["down"]
              and not c["down_right"] and not c["up_right"]):
            return 13
        elif (c["left"] and c["up"] and c["right"] and c["down"]
              and not c["down_right"] and not c["down_left"]):
            return 14
        elif (c["left"] and c["up"] and c["right"] and c["down"]
              and not c["down_left"] and not c["up_left"]):
            return 15
        elif (c["left"] and c["up"] and c["right"] and c["down"]
              and not c["up_right"] and not c["up_left"]):
            return 16
        elif (c["left"] and c["up"] and c["right"] and c["down"]
              and not c["down_left"] and not c["down_right"] and not c["up_left"] and not c["up_right"]):
            return 17
        elif c["up"] and c["left"] and not c["right"] and c["down"] and not c["up_left"] and not c["down_left"]:
            return 25
        elif c["up"] and c["left"] and c["right"] and not c["down"] and not c["up_left"] and not c["up_right"]:
            return 26
        elif c["up"] and not c["left"] and c["right"] and c["down"] and not c["up_right"] and not c["down_right"]:
            return 27
        elif not c["up"] and c["left"] and c["right"] and c["down"] and not c["down_left"] and not c["down_right"]:
            return 28
        elif (c["left"] and c["down"] and c["up"] and c["right"] and not c["down_right"]):
            return 9
        elif (c["left"] and c["down"] and c["up"] and c["right"] and not c["down_left"]):
            return 10
        elif (c["left"] and c["down"] and c["up"] and c["right"] and not c["up_right"]):
            return 11
        elif (c["left"] and c["down"] and c["up"] and c["right"] and not c["up_left"]):
            return 12
        elif (not c["left"] and not c["up"] and c["right"] and c["down"]):
            return 1
        elif (c["left"] and not c["up"] and not c["right"] and c["down"]):
            return 2
        elif (not c["left"] and c["up"] and c["right"] and not c["down"]):
            return 3
        elif (c["left"] and c["up"] and not c["right"] and not c["down"]):
            return 4
        elif (not c["left"] and c["up"] and c["right"] and c["down"]):
            return 5
        elif (c["left"] and not c["up"] and c["right"] and c["down"]):
            return 6
        elif (c["left"] and c["up"] and not c["right"] and c["down"]):
            return 7
        elif (c["left"] and c["up"] and c["right"] and not c["down"]):
            return 8
        elif not c["up"] and not c["down"] and not c["right"] and not c["left"]:
            return 18
        elif not c["up"] and not c["down"] and c["right"] and c["left"]:
            return 19
        elif c["up"] and c["down"] and not c["right"] and not c["left"]:
            return 20
        elif not c["up"] and not c["down"] and not c["right"] and c["left"]:
            return 21
        elif not c["up"] and not c["down"] and c["right"] and not c["left"]:
            return 22
        elif c["up"] and not c["down"] and not c["right"] and not c["left"]:
            return 23
        elif not c["up"] and c["down"] and not c["right"] and not c["left"]:
            return 24
        else:
            return " "

    @staticmethod
    def import_map(path) -> None:
        """Import a .ods map file into a in game environment."""
        map_file = pl.Document(path)
        map_file.connect()
        sheet = map_file[0]

        tile_map = []
        for y in range(2, 13):
            st = ""
            for x in ascii_uppercase[1:24]:
                cell = sheet[x + str(y)]
                if cell.value == "":
                    st += " "
                else:
                    st += cell.value.upper()
            tile_map.append(st)

        level_name = sheet['AD2'].value
        lifes = sheet['AA1'].value
        standart_arrows = sheet['AA2'].value
        fast_arrows = sheet['AA3'].value
        piercing_arrows = sheet['AA4'].value
        bounce_arrows = sheet['AA5'].value
        level = {
            'level_name': level_name,
            'lifes': int(lifes),
            'arrows': {
                'standart_arrows': int(standart_arrows),
                'fast_arrows': int(fast_arrows),
                'piercing_arrows': int(piercing_arrows),
                'bounce_arrows': int(bounce_arrows)
            },
            'tile_map': tile_map,
            'textures': LevelUtility.convert(tile_map)
        }
        # insert try
        return level


if __name__ == '__main__':

    import_map = LevelUtility.import_map('tile_map.ods')
    for line in import_map['textures']:
        print(line)
