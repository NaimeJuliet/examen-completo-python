'''
contador=0
contador3=0
contador2=0
negativos=0
entrada=int(input("Digite un numero "))
if(entrada %2 ==0): 
    contador2+=1
if(entrada %3 ==0):
    contador3+=1
if(entrada % 2 and entrada % 3 ==0):
    contador2=contador2+1
    contador3=contador3+1
if(entrada<0):
    negativos = negativos+1

print(f"multiplos de 2: {contador2}")
print(f"multiplos de 3: {contador3}")
print(f"negativos : {negativos}")
'''