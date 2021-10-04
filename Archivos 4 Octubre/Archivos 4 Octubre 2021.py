import os
print(os.getcwd())
os.chdir("C:\\Users\\L00423103\\Desktop")
print(os.getcwd())

def escribirUnaLinea(nombre,linea):
    miArchivo = open(nombre + ".txt","w")
    miArchivo.write(linea)
    miArchivo.close()

def leerLineaArchivo(nombre):
    miArchivo = open(nombre + ".txt","r")
    linea = miArchivo.readlines()
    print(linea)
    miArchivo.close()

def escribirDosLineas(nombre,linea1,linea2):
    miArchivo = open(nombre + ".txt","w")
    miArchivo.write(linea1)
    miArchivo.write(linea2)
    miArchivo.close()

def leeInventario(nombre):
    inventario = open(nombre + ".txt","r")
    listaInventario = inventario.readlines()
    listaInventario = quitaBackSlash(listaInventario)
    print(listaInventario)
    inventario.close()
    return listaInventario
    
def quitaBackSlash(listaSucia):
    """Recibe una lista con \n y regresa una lista sin \n"""
    listaLimpios = []
    for elemento in listaSucia:
        limpio = elemento.rstrip()
        listaLimpios.append(limpio)
    return listaLimpios
    
def escribeLista(nombre,lista):
    miArchivo = open(nombre + ".txt","w")
    miArchivo.writelines(lista)
    miArchivo.close()
    