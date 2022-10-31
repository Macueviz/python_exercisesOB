def añoBisiesto():
    año: int = int(input("Escribe un año "))
    if(año % 4 ==0):
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")

añoBisiesto()