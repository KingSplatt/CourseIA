# Arbol binario de busqueda

Este código implementa un arbol en python, en cual consiste de lo siguiente:

### clases:

- **Nodo:** Nodo del árbol, con su valor y referencias a sus hijos izquierdo y derecho.
- **Tree:** Representa el árbol y contiene métodos para insertar nodos, recorrer el árbol y buscar valores.

### métodos:

- _insertarNodo:_ Inserta un valor en el árbol. Si el árbol está vacío, crea un nodo raíz con el valor. Si no, llama al método insertar para encontrar la ubicación adecuada en el árbol.

- _insertar:_ Método recursivo para insertar valores cuando ya hay al menos 1. Si el valor es menor que el nodo actual, se mueve al subárbol izquierdo; si es mayor, al subárbol derecho.

- _preOrden, inOrden, postOrden:_ Métodos de recorrido del árbol en tres órdenes distintos:

  - Preorden: Primero el nodo, luego el subárbol izquierdo y derecho.
  - Inorden: Primero el subárbol izquierdo, luego el nodo, y finalmente el subárbol derecho.
  - Postorden: Primero los subárboles izquierdo y derecho, luego el nodo.

- _buscar:_ Método recursivo para buscar un valor en el árbol. Si el valor es encontrado en el nodo actual, devuelve True. Si es menor, busca en el subárbol izquierdo; si es mayor, en el subárbol derecho. Si no lo encuentra, devuelve False.

## Autores

- [@Peña Lopez Miguel Angel](https://github.com/KingSplatt)

- [@Robles Rios Jacquelin](https://github.com/jacq1813)
