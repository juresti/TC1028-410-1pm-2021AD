def leeArchivo(nombre):
    with open(nombre + ".txt","r") as miArchivo:
        datosSucios = miArchivo.readlines()
    
    return datosSucios

def quitaBS(listaSucia):
    lista = []
    for elem in listaSucia:
        lista.append(elem.rstrip())
    return lista

def convierteAListasInv(listaConv):
    """Recibe una lista con strings que se van a convertir en listas
        pues cada uno, tiene los datos de un producto"""
    lista = []
    for cadena in listaConv:
        lista.append(cadena.split("\t"))
    lista = lista[1:] #elimina encabezados
    return lista

def darFormatoFinalInv(listaSinFormato):
    """Recibe una lista de listas en la que hay que dar formato de tipo de dato
        a cada producto de la lista"""
    listaFormato = []
    for producto in listaSinFormato:
        idProd = int(producto[0])
        desc = producto[1]
        cant = int(producto[2])
        precio = float(producto[3])
        listaFormato.append([idProd,desc,cant,precio])
    return listaFormato
        
def leeInventario():
    """Lee del disco el inventario y lo regresa listo para ser trabajado
        por el programa (lista con listas de productos) """
    invSucio = leeArchivo("Inventario")
    #print(invSucio)
    invSinBS = quitaBS(invSucio)
    #print(invSinBS)
    invListas = convierteAListasInv(invSinBS)
    #print(invListas)
    invFinal = darFormatoFinalInv(invListas)
    #print(invFinal)
    return invFinal
    
