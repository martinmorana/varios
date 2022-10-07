from ctypes.wintypes import PINT
import yaml
import os
# /usr/bin/python3 test3.py

AMBIENTE = os.getenv('AMBIENTE')
print('el entorno es ' + AMBIENTE)
MICROSERVICIO = os.getenv('MICROSERVICIO')
print('el ms es ' + MICROSERVICIO)
MICROSERVICE_YAML = MICROSERVICIO + "/values-main.yaml" 
MICROSERVICE_CONFIGMAP_YAML = MICROSERVICIO + "/templates/configmap.yaml" 

def read_values():
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
   print(configmap_template_data)
  

   for configmap in test:
         print(configmap)
         print(test[configmap])
         data['configmap']['data'][configmap.lower()] = test[configmap]
         configmap_template_data['data'][configmap.upper()] =  "{{ default .Values.configmap.data." + str(configmap.lower()) + "}}"


   with open(MICROSERVICE_YAML, 'w') as yaml_file:
      yaml_file.write( yaml.dump(data, default_flow_style=False))
   
   with open(MICROSERVICE_CONFIGMAP_YAML, 'w') as yaml_file:
      yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))




read_values()

