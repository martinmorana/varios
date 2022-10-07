from ctypes.wintypes import PINT
import yaml
import os
import os.path

file_exists = os.path.exists('config.yaml')
if not file_exists:
   print('NO existe el archivo')
   quit()


AMBIENTE = os.getenv('AMBIENTE')
if AMBIENTE is None:   
   print('No se declaro la variable de Entorno. Termino script')
   quit()

MICROSERVICIO = os.getenv('MICROSERVICIO')
if MICROSERVICIO is None:   
   print('No se declaro la variable de Microservicio. Termino script')
   quit()


PIPELINE_ENABLED = os.getenv('PIPELINE_ENABLED')
if PIPELINE_ENABLED is None:   
   print('Este Microservicio no esta habilitado para configurar el configMap')
   quit()

MICROSERVICE_YAML = MICROSERVICIO + "/values-main.yaml" 
MICROSERVICE_CONFIGMAP_YAML = MICROSERVICIO + "/templates/configmap.yaml" 

print('Vamos a configurar el Microservicio ' + str(MICROSERVICIO) + ' en el ambiente de ' + str(AMBIENTE))

def Change_YAML():
   with open('config.yaml') as yaml_config:
      try:
         configmap_input = yaml.safe_load(yaml_config)
      except yaml.YAMLError as exc:
         print('Error al abrir el archivo config.yaml ' + str(exc))
   new_values = configmap_input[AMBIENTE]['configmap']['data']   

   values_main_yaml = open(MICROSERVICE_YAML, 'r')
   try:
      values_main_yaml_data = yaml.safe_load(values_main_yaml)
   except yaml.YAMLError as exc:
      print(exc)

   configmap_template = open(MICROSERVICE_CONFIGMAP_YAML, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)

   for configmap in new_values:
         print('Configuro la Variable de Entorno: ' + str(configmap) + ' = '+ str(new_values[configmap]))
         values_main_yaml_data['configmap']['data'][configmap.lower()] = new_values[configmap]
         configmap_template_data['data'][configmap.upper()] =  "{{ default .Values.configmap.data." + str(configmap.lower()) + "}}"

   with open(MICROSERVICE_YAML, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(values_main_yaml_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)
   
   with open(MICROSERVICE_CONFIGMAP_YAML, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

Change_YAML()

