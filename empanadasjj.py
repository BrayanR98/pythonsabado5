print("***MENU**")
print("""1. Agregar 1 empanada
         2.Mostrar Empanada
         3.SALIR""")
opcion=100
#DATOS EMPANADA
#sabor
#Ingredientes (x3)
#Precio Fabricacion
#Precio venta
empanadas=[]
while opcion!=0:
   opcion=int(input("Digite una opcion: "))
   if opcion==1:
       empanada={}
       empanada['sabor']=input("Escriba el sabor de la empanada: ") 
       empanada['ingredientes']=[]
       for n in range(3):    
           empanada['ingredientes'].append(input("Digite un ingrediente: "))
       empanada['Precio-fabricante']=int(input("Digite el precio de fabricante: "))
       empanada["Precio-venta"]=int(input("digite el precio de la empanda: "))
       empanadas.append(empanada)
       print(empanada)
   elif opcion==2:
        print(empanadas)
   elif opcion==3:
       opcion=0
   else:
       print("Digito invalido")
else:
    print("Fin")
        