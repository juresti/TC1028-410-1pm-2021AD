def listaPersonas(numPer):
    lista = []
    for veces in range(numPer):
        nombre = input(f"{veces + 1}. Nombre de la persona: ")
        lista.append(nombre)
    return lista
    
def imprimePersonas(listaP):
    for persona in listaP:
        print(persona)
        

def menuPersonas():
    print("\nBienvenido al control de personas")
    print("1) Captura personas")
    print("2) Imprime personas")
    print("3) Salir")
    op = int(input("Dime opcion: "))
    return op

def controlPersonas():
    op = 0
    listaPer = []
    while (op != 3):
        op = menuPersonas()
        print(op)
        if (op == 1):
            numP = int(input("Dime cuantas personas capturo: "))
            listaPer = listaPersonas(numP)
        elif (op == 2):
            imprimePersonas(listaPer)
        elif (op == 3):
            print("Hasta luego")
        else:
            print("Valores validos del 1 al 3")
            
            
#controlPersonas()
            
def guardaNombreEdadCivil(numPer):
    datos = []
    for num in range(1,numPer+1):
        nombre = input(f"Dime el nombre {num}: ")
        edad = int(input(f"Dime la edad {num}: "))
        edoCivil = input(f"Dime el estado civil {num}: ")
        datos.append((nombre,edad,edoCivil))
    return datos

def creaListaEdades(datos):
    edades = []
    for datoPer in datos:
        edades.append(datoPer[1])
    return edades








