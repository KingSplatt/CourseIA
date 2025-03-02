import random
import heapq

class Nodo:
    def __init__(self, puzzle, movimiento, cant_mov, manhattan, previo):
        self.cant_mov = cant_mov
        self.puzzle = puzzle
        self.movimiento = movimiento
        self.manhattan = manhattan
        self.previo = previo

puzzle = [[1,2,3],
         [4,5,6],
         [7,8,0]]

puz_objetivo = [[1, 5, 3], 
                [4, 2, 6], 
                [7, 8, 0]]


def main():
   
    inicial = Nodo(puzzle, None, 0, 0, None)
    objetivo = Nodo(puz_objetivo, None, 0, 0, None)



    print("Puzzle inicial")
    print(puzzle)

    print("Puzzle objetivo")
    print(puz_objetivo)
    
if __name__ == "__main__":
    main()