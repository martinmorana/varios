# Definicion de Variables
#numericas
entero      = 5
print(entero)
realflow    = 0.52
print (realflow)
exponente   = 0.56e-3
print (exponente)

#string
cads = 'texto entre \n\t comillas y tabulacion'
print (cads)

cads = 'texto entre \n comillas y enter'
print (cads)

cads = """Texto Linea 1
Texto Linea 2
Texto Linea 3
"""
print (cads)

cads = '''Texto Linea 1b
Texto Linea 2b
Texto Linea 3b
'''
print (cads)
# boleano
bT = True
bF = False
print (bT) 

#Listas (Se pueden modificar y agregar elimentos)
lista = [2,"tres",4,["uno",2]]
print(lista)
print(lista[1])
print(lista[0:2])
print(lista[3][1]) 
lista[0] = "1"

## Ordeno una lista con el metodo Sort
listastr = ["C","D","A","B"]
print(listastr)
listastr.sort() # Esto funciona para string
print(listastr)

## Modifico valores en la listas:
lista.append("agregado") # Agrego un valor a la lista
print(lista)

#elimino valores de la lista
del lista[0] # Elimino una valor de la lista
print(lista)

# el metodo pop elimna el ultimo valor de la lista, o el que le indiques
lista.pop()
print(lista)
lista.pop(1)
print(lista)


# imprimo una texto con el valor de una variable con el f
print(f'la lista de valores es {lista[1]}') # concateno todo

#tuplas (No se pueden cambiar, es fija)
tupla = ("1",2,True)
print(tupla) 
print(type(tupla))  
print(tupla[1])

#diccionarios (No puedo poner una tupla detro de un diccionario)
diccionar = {'clave1':[1,2,3],
             'clave2':True,
             1:"hola",
             2:True
             }

print(diccionar)
print(diccionar['clave1'])
print(diccionar[2])
diccionar[2] = False
print(diccionar[2])

# Operaciones aritmeticas
print ('operaciones aritmericas')
print (entero * realflow)
print (entero / realflow)
print (entero ** 2)


# verifico tipo de variable
print (type(entero))
