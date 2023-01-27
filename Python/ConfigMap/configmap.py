from ctypes.wintypes import PINT
import yaml
import os
import os.path


AMBIENTE = os.getenv('CI_ENVIRONMENT_NAME')

AMBIENTE = 'dev'
MS_TYPE = 'backend'

class Restaurant:

    def __init__(self,ENV,CAT): # Armo un constructor
        print('Me ejecuto automaticamente')
        self.ENV = ENV # atributo
        self.CAT = CAT # atributo
        with open('config.yaml') as yaml_config:
            try:
                new_values_main = yaml.safe_load(yaml_config)
            except yaml.YAMLError as exc:
                print('Error al abrir el archivo config.yaml ' + str(exc))
        new_values_main_data = new_values_main['configmap'][AMBIENTE]   
        print(new_values_main_data)

        values_main_yaml = 'values-main.yaml'
        values_main = open(values_main_yaml, 'r')
        try:
            values_main_data = yaml.safe_load(values_main)
        except yaml.YAMLError as exc:
            print(exc)

        configmap_yaml = 'configmap-env.yaml'
        configmap = open(configmap_yaml, 'r')
        try:
            configmap_data = yaml.safe_load(configmap)
        except yaml.YAMLError as exc:
            print(exc)

        for key, value in new_values_main_data.items():
            print(str(key),  value)
            values_main_data['configmap']['data'][str(key)] = value
            # microservice_chart_yaml = 'jcard-prepaid-'+ nombre_emisor +'-ds-external-sor/Chart.yaml'
            configmap_data['data'][str(key)] = '{{ default .Values.configmap.data.' + str(key) + ' }}'
        
        with open(values_main_yaml, 'w') as yaml_file:
            try:
                yaml_file.write( yaml.dump(values_main_data, default_flow_style=False, sort_keys=False))
            except yaml.YAMLError as exc:
                print(exc)

        with open(configmap_yaml, 'w') as yaml_file:
            try:
                yaml_file.write( yaml.dump(configmap_data, default_flow_style=False, sort_keys=False))
            except yaml.YAMLError as exc:
                print(exc)
        

    def mostar_informacion(self):
        print(f'Nombre: {self.ENV}, categoria {self.CAT}')

# instanciar la clase
restaurant = Restaurant(AMBIENTE,MS_TYPE)

# llamo al metodo de la clase
restaurant.mostar_informacion() # llamo al metodo agregar_restaurante


# Genero otro objeto instanciando la misma clase
restaurant2 = Restaurant('Parrilla','Comida Argentina')
restaurant2.mostar_informacion()



