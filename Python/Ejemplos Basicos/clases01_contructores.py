class Restaurant:

    def __init__(self,nombre,categoria): # Armo un constructor
        print('Me ejecuto automaticamente')
        self.nombre = nombre # atributo
        self.categoria = categoria # atributo

    def mostar_informacion(self):
        print(f'Nombre: {self.nombre}, categoria {self.categoria}')

# instanciar la clase
restaurant = Restaurant('Pizzeria','Comida Italiana')

# llamo al metodo de la clase
restaurant.mostar_informacion() # llamo al metodo agregar_restaurante


# Genero otro objeto instanciando la misma clase
restaurant2 = Restaurant('Parrilla','Comida Argentina')
restaurant2.mostar_informacion()



