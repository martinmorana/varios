from ctypes.wintypes import PINT
import yaml


class Restaurant:

    def __init__(self,nombre,categoria): # Armo un constructor
        print('Me ejecuto automaticamente')
        self.nombre = nombre # atributo
        self.categoria = categoria # atributo
        with open('values-main.yaml') as yaml_config:
            try:
                new_values = yaml.safe_load(yaml_config)
            except yaml.YAMLError as exc:
                print('Error al abrir el archivo config.yaml ' + str(exc))
        new_values_data = new_values['configmap']  
        print(new_values)

    def mostar_informacion(self):
        print(f'Nombre: {self.nombre}, categoria {self.categoria}')

# instanciar la clase
restaurant = Restaurant('Pizzeria','Comida Italiana')

# llamo al metodo de la clase
restaurant.mostar_informacion() # llamo al metodo agregar_restaurante


# Genero otro objeto instanciando la misma clase
restaurant2 = Restaurant('Parrilla','Comida Argentina')
restaurant2.mostar_informacion()



