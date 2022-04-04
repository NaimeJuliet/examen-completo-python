'''-Leer el año de nacimiento de 10 estudiantes del curso de Globant y
calcular cuantos años cumple cada estudiante en 2022, finalmente
indique cuantos estudiantes tienen más de 22 años (+1)
'''
estudiantes=0
contador=0

while(estudiantes<10):
    print(estudiantes)
    estudiantes+=1
    edad=int(input("digita el año en que naciste: "))
    edad=2022-edad
    print(f"su edad es {edad}")
    if(edad>=22):
        contador+=1
print(f"la cantidad de estudiantes mayores de 22 años son: {contador}")
