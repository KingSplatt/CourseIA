import random
import heapq

class Nodo:
    def __init__(self, puzzle, movimiento, cant_mov, manhattan, previo):
        self.cant_mov = cant_mov
        self.puzzle = puzzle
        self.movimiento = movimiento
        self.manhattan = manhattan
        self.previo = previo
        
def main():
    puzzle = [[1,2,3],
              [4,5,6],
              [7,8,0]]
    print("Puzzle inicial")
    print(puzzle)
    
if __name__ == "__main__":
    main()