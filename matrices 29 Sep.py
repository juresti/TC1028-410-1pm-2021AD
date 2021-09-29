def crearMatriz(numRen,numCol,valor):
    """Regresa una matriz de tamañon numRenXnumCol inicializa con el
        valor recibido"""
    matriz = []
    for ren in range(numRen): #Crear renglones
        renglon = []
        for col in range(numCol): #Añadir valores de las columnas
            renglon.append(valor)
        matriz.append(renglon)
    
    return matriz

def imprimirMatriz(matriz):
    salida = ""
    for renglon in matriz:
        for dato in renglon: #Creando un renglon en el string
            salida += str(dato) + " "
        salida += "\n" #separe el renglon en el string
    print(salida)

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
    
def tamanoMatriz(matriz):
    """Regresa una tupla (numRen, numCol) con el tamaño de la matriz"""
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for renglon in matriz: #verifica todos los reglones mismo numumero de columnas
        tam = len(renglon)
        if (tam != numCol):
            return -1,-1
    
    return numRen,numCol
    
        
    
    
