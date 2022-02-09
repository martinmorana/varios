edad = 0

while edad <= 20:
    if edad == 15:
        edad = edad + 1
        continue
    if edad == 16:
        break

    print('Tienes: ' + str(edad))
    edad = edad + 1


#######################################################

listas = ['Elemento 1','Elemento 2','Elemento 3']

for lista in listas:
    print(f"el valor de la lista es {lista}")

for numero in range(0,20):
    print(numero)