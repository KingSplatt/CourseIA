#include <bits/stdc++.h>
using namespace std;
// Splatt
#define FOR(x, n) for (int x = 0; x < (int)n; x++)
#define FOR1(x, n) for (int x = 1; x <= (int)n; x++)
#define FORR(x, n) for (int x = n - 1; x >= 0; x--)
#define FORR1(x, n) for (int x = n; x >= 1; x--)
#define deb(x) cout << #x << " = " << x << '\n';
#define deb2(x, y) cout << #x << " = " << x << ", " << #y << " = " << y << '\n';
#define pb push_back
#define eb emplace_back
#define all(x) x.begin(), x.end()
#define N "\n"

typedef unsigned long long ull;
typedef unsigned int ui;
typedef long long ll;

using ii = pair<int, int>;
using iii = tuple<int, int, int>;
using vi = vector<int>;
using vii = vector<ii>;
struct nodo
{
    int dato;
    nodo *left;
    nodo *right;
};

nodo *crearNodo(int dato)
{
    nodo *nuevoNodo = new nodo();
    nuevoNodo->dato = dato;
    nuevoNodo->left = NULL;
    nuevoNodo->right = NULL;
    return nuevoNodo;
}

void insertar(nodo *&arbol, int dato)
{
    if (arbol == NULL)
    {
        nodo *nuevoNodo = crearNodo(dato);
        arbol = nuevoNodo;
    }
    else
    {
        int valorRaiz = arbol->dato;
        if (dato < valorRaiz)
        {
            insertar(arbol->left, dato);
        }
        else
        {
            insertar(arbol->right, dato);
        }
    }
}

void preOrden(nodo *arbol)
{
    if (arbol == NULL)
    {
        return;
    }
    else
    {
        cout << arbol->dato << " - ";
        preOrden(arbol->left);
        preOrden(arbol->right);
    }
}

void inOrden(nodo *arbol)
{
    if (arbol == NULL)
    {
        return;
    }
    else
    {
        inOrden(arbol->left);
        cout << arbol->dato << " - ";
        inOrden(arbol->right);
    }
}

void postOrden(nodo *arbol)
{
    if (arbol == NULL)
    {
        return;
    }
    else
    {
        postOrden(arbol->left);
        postOrden(arbol->right);
        cout << arbol->dato << " - ";
    }
}
nodo *arbol = NULL;

int main()
{
    ios_base ::sync_with_stdio(0);
    cin.tie(NULL);
    int n;
    cin >> n;
    FOR(i, n)
    {
        int x;
        cin >> x;
        insertar(arbol, x);
    }
    cout << "PreOrden: ";
    preOrden(arbol);
    cout << N;
    cout << "InOrden: ";
    inOrden(arbol);
    cout << N;
    cout << "PostOrden: ";
    postOrden(arbol);
}