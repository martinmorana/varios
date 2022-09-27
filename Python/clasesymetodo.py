from mailbox import NoSuchMailboxError


class Restaurant: #creo una clase
    def agregar_resturante(self, nombre):    # creo un metodo
        print ('Agregando ....')
        self.nombre = nombre # Atributo
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')


# Instancio la clase
restaurant = Restaurant() # creo el objeto restaurant
restaurant.agregar_resturante('Pizzeria Llavallol')
restaurant.mostrar_informacion()

restaurant2 = Restaurant() 
restaurant2.agregar_resturante('Pizzeria Miramar')
restaurant2.mostrar_informacion()



class Restaurant_2: #creo una clase
    def __init__(self, nombre, categoria):    # Ejecuto un constructor
        self.nombre = nombre # Atributo
        self.categoria = categoria # Atributo

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria {self.categoria}')

restaurant_2 = Restaurant_2('Pizzeria Llavallol','Comida Italiana')
restaurant_2.mostrar_informacion()
restaurant_2 = Restaurant_2('Pizzeria Miramar','Comida de la costa')
restaurant_2.mostrar_informacion()

