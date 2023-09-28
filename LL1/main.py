import pandas as pd

class NodoPila:
    def __init__(self, simbolo, lexema):
        global contador
        self.simbolo = simbolo
        self.lexema = lexema
        self.id = contador + 1
        contador += 1

class NodoArbol:
    def __init__(self, id, simbolo, lexema):
        self.id = id
        self.simbolo = simbolo
        self.lexema = lexema
        self.hijos = []
        self.padre = None

def buscar_nodo(id, nodo):
    if nodo.id == id:
        return nodo
    else:
        for hijo in nodo.hijos:
            resultado = buscar_nodo(id, hijo)
            if resultado is not None:
                return resultado
        return None

def imprimir_arbol(nodo, nivel=0):
    print("  " * nivel + str(nodo.simbolo))
    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)

tabla = pd.read_csv("LL1/tabla.csv", index_col=0)
contador = 0
pila = []

simbolo_E = NodoPila('E', None)
simbolo_dolar = NodoPila('$', None)
pila.append(simbolo_dolar)
pila.append(simbolo_E)

raiz = NodoArbol(simbolo_E.id, simbolo_E.simbolo, simbolo_E.lexema)

entrada = [ 
    {"simbolo":"int", "lexema":"4", "nroline":2, "col":2},
    {"simbolo":"*", "lexema":"*", "nroline":2, "col":4},
    {"simbolo":"int", "lexema":"5", "nroline":2, "col":6},
    {"simbolo":"$", "lexema":"$", "nroline":0, "col":0},
]

i = 0
while len(pila) > 0:
    simbolo_actual = pila[-1]
    entrada_actual = entrada[i]["simbolo"]
    produccion = tabla.loc[simbolo_actual.simbolo, entrada_actual]
    if produccion == "error":
        print("Error de sintaxis")
        break
    elif produccion == "pop":
        pila.pop()
        i += 1
    else:
        pila.pop()
        for simbolo in reversed(produccion.split()):
            nodo_p = NodoPila(simbolo, None)
            pila.append(nodo_p)
            nodo_hijo = NodoArbol(nodo_p.id, nodo_p.simbolo, nodo_p.lexema)
            nodo_padre = buscar_nodo(simbolo_actual.id, raiz)
            nodo_padre.hijos.append(nodo_hijo)
            nodo_hijo.padre = nodo_padre

if i == len(entrada) and len(pila) == 0:
    print("Parse exitoso")
    imprimir_arbol(raiz)