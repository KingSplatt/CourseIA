import random
import heapq

#para cada uno de los nodos, se calcula la distancia manhattan y se agrega a la cola de prioridad
#se toma el nodo con menor peso y se expande
def busqueda_a_estrella(inicial, objetivo):
    pendientes = []
    visitados = set()
    heapq.heappush(pendientes, inicial)
    while pendientes:
        actual = heapq.heappop(pendientes)
        if actual.puzzle == objetivo.puzzle:
            return actual
        visitados.add(str(actual.puzzle))
        for vecinos in actual.encontrar_siguientes_nodos():
            if str(vecinos.puzzle) not in visitados:
                heapq.heappush(pendientes, vecinos)
    return None

# calcular la distancia manhattan |x2 - x1| + |y2 - y1|
def distancia_manhattan(puzzle, objetivo):
    distancia = 0
    posiciones_objetivo = {} #esto es un diccionario que guarda las posiciones de los valores del objetivo
    for i in range(3):
        for j in range(3):
            posiciones_objetivo[objetivo[i][j]] = (i, j)

    for i in range(3):
        for j in range(3):
            valor = puzzle[i][j]
            if valor != 0:
                objetivo_i, objetivo_j = posiciones_objetivo[valor]
                distancia += abs(objetivo_i - i) + abs(objetivo_j - j)
    return distancia

class Nodo:
    def __init__(self, puzzle, movimiento, cant_mov, manhattan, previo):
        self.cant_mov = cant_mov
        self.puzzle = puzzle
        self.movimiento = movimiento
        self.manhattan = manhattan
        self.previo = previo
    # Ocupamos un comparador para pq
    def __lt__(self, otro):
        return (self.cant_mov + self.manhattan) < (otro.cant_mov + otro.manhattan)
    # Metodo para mover la pieza
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
                siguientes_nodos.append(Nodo(nuevo_puzzle, movimiento, self.cant_mov + 1, distancia_manhattan(nuevo_puzzle,puz_objetivo ), self))  # Se agrega el nodo a la lista de nodos, pendiente se nececita implementar la distancia manhattan
        return siguientes_nodos
    
    def impimir_recorrido(self,inical):
        camino = []
        actual = self
        while actual != None:
            camino.append(actual)
            actual = actual.previo
        camino.append(inical)
        camino.reverse()
        return camino
    
    def imprimir(self):
        print("================================")
        for fila in self.puzzle:
            print(fila)
        print("================================")
        print()
        print()
        print()

        

puzzle = [[2,8,3],[1,6,4],[7,0,5]]
puz_objetivo = [[1, 5, 3], [4, 2, 6], [7, 8, 0]]

def main():
    
    inicial = Nodo(puzzle, None, 0, 0, None)
    objetivo = Nodo(puz_objetivo, None, 0, 0, None)

    print("Puzzle inicial")
    print(inicial.imprimir())

    print("Puzzle objetivo")
    print(objetivo.imprimir())

    resultado = busqueda_a_estrella(inicial, objetivo)
    
    if resultado is None:
        print("No se encontró solución")
    else:
        for nodo in resultado.impimir_recorrido(inicial):
            print("Movimiento: ", nodo.movimiento)
            print("Manhattan: ", nodo.manhattan)
            print("Cantidad de movimientos: ", nodo.cant_mov)
            nodo.imprimir()
            
        
if __name__ == "__main__":
    main()