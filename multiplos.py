numero=0
contador2=0
contador3=0
negativos=0
espacio=int(input("Digite cuantos numeros quiere "))
while(numero<espacio):
    print(numero)
    numero=numero+1
    entrada=int(input("Digite un numero "))
if(entrada %2 ==0): 
    contador2+=1
if(entrada %3 ==0):
    contador3+=1
if(entrada<0):
    negativos = negativos+1
print(f"los multiplos de 2 son : {contador2}")
print(f"los multiplos de 3 son : {contador3}")
print(f"Los números negativos son: {negativos}")     
    
    


