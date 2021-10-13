def leerAsistencia():
    with open("Asistencia.txt","r") as miArchivo:
        datosS = miArchivo.readlines()
        
    datosSB = []
    for persona in datosS:
        sinBS = persona.rstrip()
        datosSB.append(sinBS.split(","))
    
    datosFin = []
    for persona in datosSB:
        nombre = persona[0]
        asistencia = int(persona[1])
        datosFin.append([nombre,asistencia])
        
    return datosFin

def anotarAsistencia(nombre,regAsistencia):
    """Recibe el nombre de una persona y una lista con la asistencia hasta
        el momento.
        Regresa la lista de asistencia actualizada"""
    pos = 0
    encontrado = False
    for regPersona in regAsistencia: #busqueda del nombre
        if nombre in regPersona:
            regAsistencia[pos][1] += 1
            encontrado = True
            break
        pos += 1
        
    if not encontrado:
        regAsistencia.append([nombre,1])
        
    return regAsistencia

def guardaAsistenciaArchivo(datosAsistencia):
    listaParaArchivo = []
    for regPersona in datosAsistencia:    
        salida = regPersona[0] + "," #nombre
        salida += str(regPersona[1]) + "\n"
        listaParaArchivo.append(salida)
    
    print(listaParaArchivo)
    with open("Asistencia.txt","w") as miArchivo:
        miArchivo.writelines(listaParaArchivo)
        print("Archivo escrito a disco")
    
    
def main():
    datosAsistencia = leerAsistencia()
    nombre = input("Dime a quien le pones asistencia: ")
    datosAsistencia = anotarAsistencia(nombre,datosAsistencia)
    print(datosAsistencia)
    guardaAsistenciaArchivo(datosAsistencia)
    