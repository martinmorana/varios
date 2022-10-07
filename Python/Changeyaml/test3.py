from ctypes.wintypes import PINT
import yaml
import os
import os.path


import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")


file_exists = os.path.exists('config.yaml')
if not file_exists:
   print('NO existe el archivo')
   quit()


AMBIENTE = os.getenv('AMBIENTE')
if AMBIENTE is None:   
   print('\r\nNo se declaro la variable de Entorno. Termino script')
   quit()

MICROSERVICIO = os.getenv('MICROSERVICIO')
if MICROSERVICIO is None:   
   print('\r\nNo se declaro la variable de Microservicio. Termino script')
   quit()


PIPELINE_ENABLED = os.getenv('PIPELINE_ENABLED')
if PIPELINE_ENABLED is None:   
   print('\r\nEste Microservicio no esta habilitado para configurar el configMap')
   quit()

microservice_yaml = MICROSERVICIO + "/values-main.yaml" 
microservice_configmap_yaml = MICROSERVICIO + "/templates/configmap.yaml" 

print('\r\nVamos a configurar el Microservicio ' + str(MICROSERVICIO) + ' en el ambiente de ' + str(AMBIENTE))

def Change_YAML():
   with open('config.yaml') as yaml_config:
      try:
         configmap_input = yaml.safe_load(yaml_config)
      except yaml.YAMLError as exc:
         print('Error al abrir el archivo config.yaml ' + str(exc))
   new_values = configmap_input[AMBIENTE]['configmap']['data']   

   values_main_yaml = open(microservice_yaml, 'r')
   try:
      values_main_yaml_data = yaml.safe_load(values_main_yaml)
   except yaml.YAMLError as exc:
      print(exc)

   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)

   for configmap in new_values:
         print('Configuro la Variable de Entorno: ' + str(configmap) + ' = '+ str(new_values[configmap]))
         values_main_yaml_data['configmap']['data'][configmap.lower()] = new_values[configmap]
         configmap_template_data['data'][configmap.upper()] =  "{{ default .Values.configmap.data." + str(configmap.lower()) + "}}"

   with open(microservice_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(values_main_yaml_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)
   
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

Change_YAML()

