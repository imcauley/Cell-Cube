import copy
import random

class Cube:
    def __init__(self):
        self.cube = []
        self.moves = []
        for num in range(26):
            self.cube.append(num)

    def print_cube(self):
        print(self.cube)

    def turn(self, direction):
        if direction < 0:
            direction = -1 * direction
            for _ in range(3):
                self.move_pieces(direction)
        else:
            self.move_pieces(direction)

    def move_pieces(self, direction):
        C1 = copy.copy(self.cube)
        C2 = copy.copy(self.cube)

        F1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        F2 = [6, 3, 0, 7, 4, 1, 8, 5, 2]

        R1 = [2, 11, 19, 5, 12, 22, 8, 13, 25]
        R2 = [8, 5, 2, 13, 12, 11, 25, 22, 19]

        L1 = [17, 9, 0, 20, 14, 3, 23, 15, 6]
        L2 = [23, 20, 17, 15, 14, 9, 6, 3, 0]

        U1 = [17, 18, 19, 9, 10, 11, 0, 1, 2]
        U2 = [0, 9, 17, 1, 10, 18, 2, 11, 19]

        D1 = [6, 7, 8, 15, 16, 13, 23, 24, 25]
        D2 = [23, 15, 6, 24, 16, 7, 25, 13, 8]

        B1 = [19, 18, 17, 22, 21, 20, 25, 24, 23]
        B2 = [25, 22, 19, 24, 21, 18, 23, 20, 17]

        if(direction == 1):
            for p in range(9):
                C1[F1[p]] = C2[F2[p]]
        elif(direction == 2):
            for p in range(9):
                C1[R1[p]] = C2[R2[p]]
        elif(direction == 3):
            for p in range(9):
                C1[L1[p]] = C2[L2[p]]
        elif(direction == 4):
            for p in range(9):
                C1[U1[p]] = C2[U2[p]]
        elif(direction == 5):
            for p in range(9):
                C1[D1[p]] = C2[D2[p]]
        elif(direction == 6):
            for p in range(9):
                C1[B1[p]] = C2[B2[p]]

        self.cube = C1

    def scramble(self):

        for x in range(26):
            direction = random.randint(1,6)
            prime = random.randint(0,1)
            if prime:
                direction = -1 * direction
            self.turn(direction)
            self.moves.append(direction)

    def get_cube(self):
        return tuple(self.cube)
