from ctypes.wintypes import PINT
import yaml
import os
import os.path
import shutil
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


print('\r\nVamos a configurar el Microservicio ' + str(MICROSERVICIO) + ' en el ambiente de ' + str(AMBIENTE))

def Copy_folders():
   # Providing the folder path
   print('Genero las carpeta del emisor: ' + str(nombre_emisor))
   src = 'jcard-prepaid-bimo-app'
   dest = 'jcard-prepaid-'+ nombre_emisor +'-app'
   print('Copy folder: ' + src + ' to ' + dest)
   try:
      destination = shutil.copytree(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))
   
   
   src = 'jcard-prepaid-bimo-ds-external-sor'
   dest = 'jcard-prepaid-'+ nombre_emisor +'-ds-external-sor'
   print('Copy folder: ' + src + ' to ' + dest)
   try:
      destination = shutil.copytree(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))

   src = 'jcard-prepaid-bimo-invoice'
   dest = 'jcard-prepaid-'+ nombre_emisor +'-invoice'
   print('Copy folder: ' + src + ' to ' + dest)
   try:
      destination = shutil.copytree(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))

   src = 'jcard-prepaid-bimo-jcard'
   dest = 'jcard-prepaid-'+ nombre_emisor +'-jcard'
   print('Copy folder: ' + src + ' to ' + dest)
   try:
      destination = shutil.copytree(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))

   src = 'jcard-prepaid-bimo-restapi'
   dest = 'jcard-prepaid-'+ nombre_emisor +'-restapi'
   print('Copy folder: ' + src + ' to ' + dest)
   try:
      destination = shutil.copytree(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))
   
   

def Read_YAML():
   global nombre_emisor
   global port_emisor
   global database_emisor
   with open('config.yaml') as yaml_config:
      try:
         new_values_issuer = yaml.safe_load(yaml_config)
      except yaml.YAMLError as exc:
         print('Error al abrir el archivo config.yaml ' + str(exc))
   new_values_issuer_data = new_values_issuer[AMBIENTE]  
   nombre_emisor = new_values_issuer_data['nombre'].lower()
   port_emisor = new_values_issuer_data['port']
   database_emisor = new_values_issuer_data['database'].lower()
   


def Change_YAML():
   microservice_configmap_yaml = 'jcard-prepaid-'+ nombre_emisor +'-app/values-main.yaml' 
   print('Configurando el file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['database']['name'] = database_emisor
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

   microservice_configmap_yaml = 'jcard-prepaid-'+ nombre_emisor +'-invoice/values-main.yaml' 
   print('Configurando el file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['database']['name'] = database_emisor
   configmap_template_data['config']['jcard_issuer_name'] = nombre_emisor.upper()
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

   microservice_configmap_yaml = 'jcard-prepaid-'+ nombre_emisor +'-jcard/values-main.yaml' 
   print('Configurando el file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['database']['name'] = database_emisor
   configmap_template_data['jcard']['issuer_name'] = nombre_emisor.upper()
   configmap_template_data['jcard']['server_port'] = port_emisor
   configmap_template_data['services']['jcard']['port'] = port_emisor
   configmap_template_data['services']['jcard']['target_port'] = port_emisor
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)
   microservice_configmap_yaml = 'jcard-prepaid-'+ nombre_emisor +'-restapi/values-main.yaml' 
   print('Configurando el file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['database']['name'] = database_emisor
   configmap_template_data['configmap']['issuer_name'] = nombre_emisor.upper()
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)


 

 



Read_YAML()
Copy_folders()
Change_YAML()