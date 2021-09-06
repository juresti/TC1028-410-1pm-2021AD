def calculaPromedio(cuantas):
    suma = 0
    for numMat in range(1,cuantas+1):
        cal = int(input(f"Dime calificacion materia {numMat}: "))
        suma += cal
    prom = suma / cuantas
    return prom

def main():
    print("Programa que calcula promedio de calificaciones")
    num = int(input("Dime cuantas materias llevas: "))
    promedio = calculaPromedio(num)
    print(f"El promedio de tus {num} materias es de {promedio}")
    
    
def creaLinea(ancho):
    salida = "" #string vacio
    for veces in range(ancho):
        salida += "*" #concatenación
    return salida

def creaCubo(ancho,alto):
    cubo = ""
    for num in range(alto):
        cubo += creaLinea(ancho) + "\n"
    return cubo

def main2():
    print("Funcion que crea una linea del ancho deseado")
    wide = int(input("Dime el ancho de tu linea: "))
    linea = creaLinea(wide)
    print(linea)
    
def main3():
    print("Funcion que genera un cubo de ancho y alto deseado")
    wide = int(input("Dime el ancho que deseas: "))
    height = int(input("Dime el alto deseado: "))
    miCubo = creaCubo(wide,height)
    print(miCubo)
    
    
def primo(num):
    for divisor in range(2,num):
        res = num % divisor
        if (res == 0):
            return False
    return True

def primos(num):
    cont = 1
    while(cont <= num):
        if(primo(cont)):
            ultPrimo = cont
            #print(ultPrimo)
        cont += 1
    return ultPrimo

def primosVer2(num):
    cont = num
    while(cont > 0):
        if(primo(cont)):
            return cont
        cont -= 1

def creaLineaEspacios(ancho):
    linea = "*"
    for veces in range(ancho - 2):
        linea += " "
    linea += "*"
    return linea
