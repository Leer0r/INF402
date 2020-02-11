from random import randint


class Takuzu():
    def __init__(self, x):
        # Grille de x par x remplis de 2 (2 : case vide)
        self.tab_takuzu = [[2 for i in range(x)] for i in range(x)]
        self.x = x

    def affiche_tab(self):
        for i in range(self.x):
            for j in range(self.x):
                print(self.tab_takuzu[i][j], end=" ")
            print()

    def get_line(self, line: int) -> list:
        if line > self.x:
            raise IndexError("Index out of range : {}".format(line))
        return self.tab_takuzu[line]

    def get_random(self, minimum, maximum: int) -> int:
        return randint(minimum, maximum)

    def Nb(self, line: list) -> int:
        return (len([x for x in line if x == 0]), len([x for x in line if x == 1]))

    def cond1(self, line: list, info: tuple) -> bool:
        return info[0] <= (self.x)/2 and info[1] <= (self.x)/2

    def gen_table(self) -> list:
        for i in range(self.x):
            self.current_line = self.get_line(i)
            self.tuple_info = self.Nb(i)
            for j in range(self.x):
                pass


tab = Takuzu(5)
tab.affiche_tab()
