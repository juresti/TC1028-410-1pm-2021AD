def esCuadrada(matriz):
    """Regresa True si la matriz es cuadrada"""
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for renglon in matriz:
        tam = len(renglon)
        if (tam != numCol):
            return False
    
    if (numRen == numCol): #Verifica que sean iguales numRen y numCol
        return True
    else:
        return False


def sumaMatrices(mat1,mat2):
    if (esCuadrada(mat1) and esCuadrada(mat2)):
        numRen = len(mat1)
        numCol = len(mat1[0])
        mat3 = []
        for posRen in range(numRen):
            renglon = []
            for posCol in range(numCol):
                suma = mat1[posRen][posCol] + mat2[posRen][posCol]
                renglon.append(suma)
            mat3.append(renglon)
        return mat3
    else:
        return "Error: la matrices no son cuadradas"
    
def pares(lista):
    cont = 0
    for num in lista:
        if (num % 2) == 0:
            cont += 1
    return cont

def capturaLista():
    resp = input("Quieres añadir un elemento a la lista? (si/no)  ")
    lista = []
    while (resp.lower() == "si"):
        elem = input("Dime el elemento: ")
        lista.append(elem)
        resp = input("Quieres añadir un elemento a la lista? (si/no)  ")
    return lista

def ejercicio1():
    print("Ejercicio 1 - Pares")
    print("Dime la lista de elementos")
    lista = capturaLista()
    listaInt = []
    for elem in lista:
        listaInt.append(int(elem))
    numPares = pares(listaInt)
    print(f"Los pares en la lista {listaInt} son {numPares}")
    
def menu():
    print("++++++++++++   Menu   +++++++++++++++")
    print("1. Captura lista")
    print("2. Ejercicio 1")
    print("3. Salir")
    opcion = int(input("Dime tu opcion: "))
    return opcion
    
def main():
    op = 0
    while (op != 3):
        op = menu()
        if (op == 1):
            capturaLista()
        elif (op == 2):
            ejercicio1()
        elif (op == 3):
            res = input("Seguro que desea salir? (si/no)   ")
            if (res.lower() == "si"):
                print("Gracias por usar el programa")
            else:
                op = 0
        else:
            print("Opciones validas 1, 2 y 3")
    print("Programa terminado")
    
main()