'''PUNTO 3 -Construir un programa para ir de compras en un supermercado que
permita la construcción del siguiente MENÚ:

1. Digitar 1 para registrar el nombre de un producto en una lista (+0.4)
2. Digitar 2 para mostrar todos los productos registrados (+0.4)
3. Digitar 3 para permitir buscar un producto y cambiar el nombre de este (+0.4)
4. Digitar 4 para permitir buscar por nombre un producto y eliminar el producto (+0.4)
5. Digitar 0 para SALIR'''

productos=[]

while(True):

    print("**********************************")
    print("           Bienvenido             ")
    print("              MENÚ                ")
    print("**********************************")
    print("1--> Registrar producto. ")
    print("2--> Mostrar producto. ")
    print("3--> Buscar y cambiar producto. ")
    print("4--> Buscar y eliminar producto. ")
    print("0--> SALIR ")
    print("**********************************")

    opcion=int(input("Ingrese una opción : "))
    print("***********************************")
    print("***********************************")

    if(opcion==1):
        producto=input("Ingrese nombre del producto: ")
        productos.append(producto)

    elif(opcion==2):
        print (productos)

    elif(opcion==3):
        print (productos)
        productoCambiar=input("Ingrese producto a cambiar: ")
        estaProducto=False
        for i in range(0,len(productos)):
            
            if(productoCambiar==productos[i]):
                productoNuevo=input("Ingrese producto nuevo: ")
                productos[i]=productoNuevo
                print(productos) 
                estaProducto=True

        if(estaProducto==False):
            print("Producto no registrado")  
    elif(opcion==4):
        print (productos)
        productoEliminar=input("Ingrese producto a eliminar: ")
        bandera=True
        for i in range(0,len(productos)):
            if(productoEliminar==productos[i]):
                productos.pop(i)
                bandera=True
            else:
                bandera=False
        if(bandera==False):
            print("producto sin registro")    
        print(productos)

    elif(opcion==0):
        print("Gracias por su compra...")
        break

    else:
        print("ingrese una opción válida. ")