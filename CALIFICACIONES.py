print("CALIFICACIONES")

while True:
    
    nombre = input("escribe el nombre del estudiante")
    edad = int(input("escribe su edad"))
    cal = float(input("escribe su calificacion"))
    
    if cal  >= 8:
        print("felicidades" , nombre , "has tenido una calificacion excelente")
    elif cal >= 6:
        print("felicidades" , nombre , "has aprobado")

    else:
        print("lo sentimos" , nombre , "has reprobado")
        
    
    final = input("volver a calcular el promedio?")
    if final == "no":
        print("adios bro")
        break