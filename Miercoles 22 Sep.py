def listaPersonas(numPer):
    lista = []
    for veces in range(numPer):
        nombre = input(f"{veces + 1}. Nombre de la persona: ")
        lista.append(nombre)
    return lista
    