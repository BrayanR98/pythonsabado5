tupla=(1,2,3,4,5)
print(tupla)
for numero in tupla:
    print(numero)
    
#Transformando una tupla en una lista
lista=list(tupla)
print(lista)
lista.append(100)
tupla=tuple(lista)

listap=[50,45,20,30,40,87]
for i,n in enumerate(listap):
    if(n<40):
        listap.pop(i)
    
stupla=tuple(listap)
print(stupla)

lista1=[50,45,20,30,40,87]
for n in lista1:
    if n%2 !=0:
        lista1.remove(n)
        
ptupla=tuple(lista1)
print(ptupla)