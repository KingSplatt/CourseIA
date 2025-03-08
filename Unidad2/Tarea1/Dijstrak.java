import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet;
/*
 * PEÑA LOPEZ MIGUEL ANGEL 
 * 9:00-10:00 AM
 * Dr.Clemente Garcia Gerardo
 */

public class Dijstrak {
	public static void main(String[] args) throws IOException {
		Grafo grafo = new Grafo();
		try {
			FileReader fr = new FileReader("./Caminos.cvs.txt");
			BufferedReader br = new BufferedReader(fr);
			String linea = br.readLine();
			System.out.println("Ingrese el Pueblo desde donde iniciara el recorrido: ");
			Scanner sc = new Scanner(System.in);
			int Nodo = sc.nextInt();
			grafo.addNodo(Nodo);
			linea = br.readLine();
			while (linea != null) {
				String[] datos = linea.split(",");
				String nodoInicial = datos[0];
				String nodoFinal = datos[1];
				String peso = datos[2];
				grafo.addDobleArista(Integer.parseInt(nodoInicial), Integer.parseInt(nodoFinal),
						Integer.parseInt(peso));
				linea = br.readLine();
			}
			br.close();
			fr.close();
			System.out.println("Recorrido desde el pueblo: " + Nodo);
			System.out.println("Cdad Prev | Cdad Act | Km");
			for (Integer nodo : grafo.grafo.keySet()) {
				if (!nodo.equals(Nodo)) {
					grafo.verificar(Nodo, nodo);
					System.out.println();
					grafo.imprimirCamino(Nodo, nodo);
				}
			}
			sc.close();
		} catch (IOException e) {
			System.out.println("No se encontro el archivo");
		}
	}
}

class Grafo {
	TreeMap<Integer, TreeSet<Pair>> grafo = new TreeMap<Integer, TreeSet<Pair>>(); // (1,(2,40))
	TreeMap<Integer, TreeSet<Pair>> padre = new TreeMap<Integer, TreeSet<Pair>>();

	// Metodo que agrega los nodos
	public void addNodo(Integer nodo) {
		grafo.put(nodo, new TreeSet<Pair>());
	}

	// Metodo que agrega caminos entre los nodos
	public void addAristas(Integer nodoEntrada, Integer nodoSalida, Integer peso) {
		if (!grafo.containsKey(nodoSalida)) {
			addNodo(nodoSalida);

		}
		if (!grafo.containsKey(nodoEntrada)) {
			addNodo(nodoEntrada);
		}
		TreeSet<Pair> aristas = grafo.get(nodoSalida);
		aristas.add(new Pair(nodoEntrada, peso));
		grafo.replace(nodoSalida, aristas);
	}

	// Metodo que agrega caminos entre los nodos (bidireccional)
	public void addDobleArista(Integer nodoSalida, Integer nodoEntrada, Integer peso) {
		addAristas(nodoEntrada, nodoSalida, peso);
		addAristas(nodoSalida, nodoEntrada, peso);
	}

	// Metodo que verifica si existe un camino entre los nodos
	public Integer verificar(Integer NodoInicio, Integer NodoFinal) {
		if (procesar(NodoInicio, NodoFinal) == null) {
			System.out.print(" No se encontro un camino para llegar a ese nodo ");
		}
		return procesar(NodoInicio, NodoFinal);
	}

	// Metodo que imprime el camino entre los nodos
	public void imprimirCamino(Integer nodoInicial, Integer nodoFinal) {
		for (Pair par : padre.get(nodoFinal)) { // se recorre el arbol en busca de los vecinos del nodo
			if (par.getPrimero() == nodoInicial) {
				System.out.printf("%7d %7d %9d", par.getPrimero(), nodoFinal, par.getSegundo());
			} else {
				System.out.printf("%7d %7d %9d", par.getPrimero(), nodoFinal, par.getSegundo());
			}
		}
	}

	public Integer borrarNodos(Integer nodo) {
		grafo.remove(nodo);
		return nodo;
	}

	// Metodo para aplicar el Dijkstra
	public Integer procesar(Integer nodoInicial, Integer nodoObjetivo) {
		final Integer INF = Integer.MAX_VALUE;
		TreeMap<Integer, Integer> distancia = new TreeMap<Integer, Integer>(); // este se encargara de guardar la
																				// distancia
		for (Integer llave : grafo.keySet()) {
			distancia.put(llave, INF);
		}

		distancia.replace(nodoInicial, 0);
		PriorityQueue<Pair> pq = new PriorityQueue<>();
		pq.add(new Pair(0, nodoInicial));

		while (!pq.isEmpty()) {
			Pair tope = pq.poll();
			Integer dist = tope.getPrimero(), nodo = tope.getSegundo();

			if (dist > distancia.get(nodo)) {// si la distancia es mayor a la del nodo, se descarta
				continue;
			}
			for (Pair par : grafo.get(nodo)) {// se recorre el arbol en busca de los vecinos del nodo
				Integer vecino = par.getPrimero(), peso = par.getSegundo();

				if (dist + peso >= distancia.get(vecino)) {
					continue;
				}
				Integer nuevoPeso = dist + peso;
				distancia.replace(vecino, nuevoPeso);
				padre.put(vecino, new TreeSet<Pair>());
				padre.get(vecino).add(new Pair(nodo, nuevoPeso));
				pq.add(new Pair(nuevoPeso, vecino));
			}
		}
		if (distancia.get(nodoObjetivo) == INF) {
			return null;
		}
		return distancia.get(nodoObjetivo);
	}

	// en dado caso que se quiera saber el camino que se recorrio con menor peso
	public void recorrido(Integer nodoInicial, Integer nodoFinal) {
		ArrayList<Integer> recorrido = new ArrayList<Integer>();
		Integer nodo = nodoFinal;
		while (nodo != nodoInicial) {
			recorrido.add(nodo);
			nodo = grafo.get(nodo).first().getPrimero();
		}
		recorrido.add(nodoInicial);
		Collections.reverse(recorrido);
		System.out.println("Recorrido: " + recorrido);
	}
}

// Clase Pair para poder comparar los nodos (signodo,peso)
class Pair implements Comparable<Pair> {
	public int primero;
	public int segundo;

	public Pair(int primero, int segundo) {
		this.primero = primero;
		this.segundo = segundo;
	}

	// Comparable para ordenar los dos elementos
	@Override
	public int compareTo(Pair o) {
		if (primero > o.primero) {
			return 1;
		} else if (primero < o.primero) {
			return -1;
		}
		return Integer.compare(segundo, o.segundo);
	}

	public int getPrimero() {
		return primero;
	}

	public void setPrimero(int primero) {
		this.primero = primero;
	}

	public int getSegundo() {
		return segundo;
	}

	public void setSegundo(int segundo) {
		this.segundo = segundo;
	}
}