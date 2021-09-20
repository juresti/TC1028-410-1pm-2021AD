def preguntas():
    res = input("Colon descubrio América? (Si/no)  ")
    res = res.capitalize()
    print(res)
    if(res == "Si"):
        print("Bien hecho")
        
def masDeUna(pal,let):
    cont = 0
    let = let.lower()
    for letra in pal.lower():
        if (letra == let):
            cont += 1
    if (cont > 1):
        return True
    else:
        return False