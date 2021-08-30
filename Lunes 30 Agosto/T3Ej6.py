def teatro():
    sumaDesc = 0
    edad = int(input("Dime la edad: "))
    while (edad > 0):
        if(5 <= edad <= 14):
            desc = 35
        elif(15 <= edad <=19):
            desc = 25
        elif(20 <= edad <= 45):
            desc = 10
        elif(45 <= edad <= 65):
            desc = 25
        elif(edad >= 66):
            desc = 35
            
        print(f"Tu descuento es del {desc}%")
        sumaDesc += 200 * (desc / 100)
        edad = int(input("Dime la edad: "))
        
    print(f"Cantidad total por descuentos: {sumaDesc}")