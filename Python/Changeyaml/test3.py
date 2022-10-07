from ctypes.wintypes import PINT
import yaml
import os


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
      configmap_input = yaml.safe_load(yaml_config)
   test = configmap_input[AMBIENTE]['configmap']['data']

   
   stream = open(MICROSERVICE_YAML, 'r')
   data = yaml.safe_load(stream)

   configmap_template = open(MICROSERVICE_CONFIGMAP_YAML, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   

   for configmap in test:
         print('Configuro la Variable de Entorno: ' + str(configmap) + ' = '+ str(test[configmap]))
         data['configmap']['data'][configmap.lower()] = test[configmap]
         configmap_template_data['data'][configmap.upper()] =  "{{ default .Values.configmap.data." + str(configmap.lower()) + "}}"


   with open(MICROSERVICE_YAML, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)
   
   with open(MICROSERVICE_CONFIGMAP_YAML, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

Change_YAML()

