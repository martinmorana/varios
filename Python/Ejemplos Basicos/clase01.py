class Restaurant:
    def agregar_restaurante(self,nombre): # creo el metodo agregar_restaurante
        self.nombre = nombre # atributo

    def mostar_informacion(self):
        print(f'Nombre: {self.nombre}')

# instanciar la clase
restaurant = Restaurant()

# llamo al metodo de la clase
restaurant.agregar_restaurante('Pizzeria') # llamo al metodo agregar_restaurante
restaurant.mostar_informacion() # llamo al metodo mostrar_informacion

# Genero otro objeto instanciando la misma clase
restaurant2 = Restaurant()
restaurant2.agregar_restaurante('Parrilla')
restaurant2.mostar_informacion() # llamo al metodi mostrar_informacion


#llamo a los metodos de las clases:
print(f'Nombre Restaurante: {restaurant.nombre}')
print(f'Nombre Restaurante: {restaurant2.nombre}')
