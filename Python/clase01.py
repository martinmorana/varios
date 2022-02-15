class Restaurant:
    def agregar_restaurante(self,nombre): # creo el metodo agregar_restaurante
        self.nombre = nombre # atributo

# instanciar la clase
restaurant = Restaurant()

# llamo al metodo de la clase
restaurant.agregar_restaurante('Pizzeria')
