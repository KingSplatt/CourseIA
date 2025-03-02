## Tarea 8 puzzle

El rompecabezas o puzzle 8 es un problema de programación que consisten en un tipico juego de niños que jugabamos antes en la que en un cuadrilatero de 3x3 con ocho piezas y un espacio vacio tenias que reorganizar las piezas hasta una posicion objetivo a travez de movimientos deslizantes.

usualmente el estado inicial se establece de forma aleatoria , y el jugador puede mover las piezas hacia el espacio vacio, una pieza ala vez, Para la resolución de este problema se han implementado diferentes soluciones con heuristicas:

### Que es la heuristica:

La heuristica es la capacidad de las personas para descubrir, inventar o resolver problemas mediante la creatividad o pensamiento lateral

hay diferentes heuristicas para ese problema, entre ellos

- Suma total de fichas descolocadas
- Suma de distancias de manhattan
- Suma de secuencias
- Distancia euclidiana

## Metodo seleccionado: Distancia de manhattan

Como funciona este metodo, es una medida heurística usada en la búsqueda informada o la busqueda A\* (estrella) , que calcula el número total de movimientos horizontales y verticales necesarios para colocar cada numero en su posicion correcta: Sigue la siguiente formula: NΣi=1 ( |xActual - xObjetivo| + |yActual - yObjetivo| )

## La busqueda A\* (A estrella)

Es un algoritmo de búsqueda informada que encuentra el camino óptimo desde un estado inicial hasta un estado objetivo. Se basa en la funcion de costo:
F(n) = g(n) + h(n)
g(n) = hosto acumulado desde el estado inicial hasta n numero de movimientos
h(n) = heuristica que estima el costo desde n hasta la solucion, (la distancia manhattan)
F(n) = suma de ambos costos priorizando los estados que tengan menos personas

## Autores

- [@Peña Lopez Miguel Angel](https://github.com/KingSplatt)

- [@Robles Rios Jacquelin](https://github.com/jacq1813)
