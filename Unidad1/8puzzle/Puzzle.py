import random
import heapq


    #para cada uno de los nodos, se calcula la distancia manhattan y se agrega a la cola de prioridad
    #se toma el nodo con menor peso y se expande
def busqueda_a_estrella(inicial, objetivo):
        visitados = set()
        pendientes = []
        

        return None

# calcular la distancia manhattan |x2 - x1| + |y2 - y1|
def distancia_manhattan(puzzle, objetivo):
    distancia = 0
    
    return distancia

class Nodo:
    def __init__(self, puzzle, movimiento, cant_mov, manhattan, previo):
        self.cant_mov = cant_mov
        self.puzzle = puzzle
        self.movimiento = movimiento
        self.manhattan = manhattan
        self.previo = previo

#  Metodo para mover la pieza
    def mover_pieza(self, movimiento):
        puzzle = self.puzzle
        nuevo_puzzle = []
        
        for i in range(3):
            nuevo_puzzle.append(puzzle[i].copy())
            
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] == 0:
                    x, y = i, j
                    break
        
        # Mover la pieza en la dirección indicada
        if movimiento == 'arriba' and x > 0: # 0 es el límite de la matriz
            nuevo_puzzle[x][y], nuevo_puzzle[x - 1][y] = nuevo_puzzle[x - 1][y], nuevo_puzzle[x][y]
            return nuevo_puzzle
        elif movimiento == 'abajo' and x < 2: # 2 es el límite de la matriz
            nuevo_puzzle[x][y], nuevo_puzzle[x + 1][y] = nuevo_puzzle[x + 1][y], nuevo_puzzle[x][y]
            return nuevo_puzzle
        elif movimiento == 'izquierda' and y > 0: # 0 es el límite de la matriz
            nuevo_puzzle[x][y], nuevo_puzzle[x][y - 1] = nuevo_puzzle[x][y - 1], nuevo_puzzle[x][y]
            return nuevo_puzzle
        elif movimiento == 'derecha' and y < 2: # 2 es el límite de la matriz
            nuevo_puzzle[x][y], nuevo_puzzle[x][y + 1] = nuevo_puzzle[x][y + 1], nuevo_puzzle[x][y]
            return nuevo_puzzle
        return None

    # Metodo para encontrar el nodo siguiente
    def encontrar_siguientes_nodos(self):
        siguientes_nodos = []
        movimientos = ['arriba', 'abajo', 'izquierda', 'derecha']
        for movimiento in movimientos:
            nuevo_puzzle = self.mover_pieza(movimiento)
            if nuevo_puzzle is not None:
                siguientes_nodos.append()  # Se agrega el nodo a la lista de nodos, pendiente se nececita implementar la distancia manhattan
        return siguientes_nodos

puzzle = [[1,2,3],
            [4,5,6],
            [7,8,0]]
puz_objetivo = [[1, 5, 3], 
                    [4, 2, 6], 
                    [7, 8, 0]]

def main():
    
    inicial = Nodo(puzzle, None, 0, 0, None)
    bjetivo = Nodo(puz_objetivo, None, 0, 0, None)

    print("Puzzle inicial")
    print(puzzle)

    print("Puzzle objetivo")
    print(puz_objetivo)

    resultado = busqueda_a_estrella(inicial, objetivo)
        
if __name__ == "__main__":
        main()