diccionario={
    # 'nombre':"Juan",
    # 'edad':33,
    # 'Hincha-verde':True,
    # 'comidasFavoritas':['yogur','arandanos','alpiste']
}

diccionario['nombre']=input("Digite su nombre: ")
diccionario['edad']=input("digite su edad: ")
diccionario['Hincha-verde']= input("digite si le gusta el verde")
diccionario['comidasFavoritas']=input("digita su comida favorita")

print(diccionario)
print(diccionario['nombre'])
print(diccionario['comidasFavoritas'])
for llave,valor in diccionario.items():
    print(llave)
    print(valor)
    