from ctypes.wintypes import PINT
import yaml
import os
import os.path
import shutil
import sys
import secrets
import psycopg2

password_length = 16
postgrespassword = secrets.token_urlsafe(password_length)
#print(postgrespassword)

# total arguments
n = len(sys.argv)
#print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")


file_exists = os.path.exists('../../config.yaml')
if not file_exists:
   print('NO existe el archivo')
   quit()



AMBIENTE = os.getenv('CI_ENVIRONMENT_NAME')
if AMBIENTE is None:   
   print('\r\nNo se declaro la variable de Entorno. Termino script')
   quit()


DB_USER = os.getenv('DB_USER')
if DB_USER is None:   
   print('\r\nError - DB_USER variable not configure')
   quit()

DB_PASSWORD = os.getenv('DB_PASSWORD')
if DB_PASSWORD is None:   
   print('\r\nError - DB_PASSWORD variable not configure')
   quit()
DB_HOST = os.getenv('DB_HOST')
if DB_HOST is None:   
   print('\r\nError - DB_HOST variable not configure')
   quit()


print('\r\nStarting Python script. Creating Issuer in ' + str(AMBIENTE) +' environment')

def Copy_folders():
   # Providing the folder path
   print('Genero las carpeta del emisor: ' + str(nombre_emisor))
   src = 'jcard-prepaid-xperience-app'
   dest = 'jcard-prepaid-'+ nombre_emisor +'-app'
   print('Copy folder: ' + src + ' to ' + dest)
   try:
      destination = shutil.copytree(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))
   
   if external_sor == True:
      print('Creo el  microservicio ds-external-sor')
      src = 'jcard-prepaid-bimo-ds-external-sor'
      dest = 'jcard-prepaid-'+ nombre_emisor +'-ds-external-sor'
      print('Copy folder: ' + src + ' to ' + dest)
      try:
         destination = shutil.copytree(src, dest) 
      except OSError as exc:
         print('Error copy files ' + str(exc))

   src = 'jcard-prepaid-xperience-invoice'
   dest = 'jcard-prepaid-'+ nombre_emisor +'-invoice'
   print('Copy folder: ' + src + ' to ' + dest)
   try:
      destination = shutil.copytree(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))

   src = 'jcard-prepaid-xperience-jcard'
   dest = 'jcard-prepaid-'+ nombre_emisor +'-jcard'
   print('Copy folder: ' + src + ' to ' + dest)
   try:
      destination = shutil.copytree(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))
   
   
   removefile = dest + '/templates/service-account.yaml'
   print('Remove file: ' + removefile)
   if os.path.exists(removefile):
      os.remove(removefile)
   else:
      print(removefile + ' not exist')

   src = 'jcard-prepaid-xperience-restapi'
   dest = 'jcard-prepaid-'+ nombre_emisor +'-restapi'
   print('Copy folder: ' + src + ' to ' + dest)
   try:
      destination = shutil.copytree(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))
   
   

def Read_YAML():
   global nombre_emisor
   global port_emisor
   global database_emisor, service_account, external_sor, create_db
   with open('../../config.yaml') as yaml_config:
      try:
         new_values_issuer = yaml.safe_load(yaml_config)
      except yaml.YAMLError as exc:
         print('Error al abrir el archivo config.yaml ' + str(exc))
   new_values_issuer_data = new_values_issuer[AMBIENTE]  
   nombre_emisor = new_values_issuer_data['nombre'].lower()
   create_db = new_values_issuer_data['create_db']
   external_sor = new_values_issuer_data['external-sor']
   port_emisor = new_values_issuer_data['port']
   database_emisor = new_values_issuer_data['database'].lower()
   service_account = new_values_issuer_data['service_account'].lower()


def Change_YAML():


   microservice_chart_yaml = 'jcard-prepaid-'+ nombre_emisor +'-app/Chart.yaml' 
   print('Configuring file: ' + microservice_chart_yaml) 
   microservice_chart = open(microservice_chart_yaml, 'r')
   try:
      microservice_chart_data = yaml.safe_load(microservice_chart)
   except yaml.YAMLError as exc:
      print(exc)
   microservicename = nombre_emisor.lower() + '-jcard-app'
   microservice_chart_data['name'] = microservicename
   with open(microservice_chart_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(microservice_chart_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

   microservice_chart_yaml = 'jcard-prepaid-'+ nombre_emisor +'-invoice/Chart.yaml' 
   print('Configuring file: ' + microservice_chart_yaml) 
   microservice_chart = open(microservice_chart_yaml, 'r')
   try:
      microservice_chart_data = yaml.safe_load(microservice_chart)
   except yaml.YAMLError as exc:
      print(exc)
   microservicename = nombre_emisor.lower() + '-jcard-invoice'
   microservice_chart_data['name'] = microservicename
   with open(microservice_chart_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(microservice_chart_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

   microservice_chart_yaml = 'jcard-prepaid-'+ nombre_emisor +'-jcard/Chart.yaml' 
   print('Configuring file: ' + microservice_chart_yaml) 
   microservice_chart = open(microservice_chart_yaml, 'r')
   try:
      microservice_chart_data = yaml.safe_load(microservice_chart)
   except yaml.YAMLError as exc:
      print(exc)
   microservicename = nombre_emisor.lower() + '-jcard'
   microservice_chart_data['name'] = microservicename
   with open(microservice_chart_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(microservice_chart_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

   microservice_chart_yaml = 'jcard-prepaid-'+ nombre_emisor +'-restapi/Chart.yaml' 
   print('Configuring file: ' + microservice_chart_yaml) 
   microservice_chart = open(microservice_chart_yaml, 'r')
   try:
      microservice_chart_data = yaml.safe_load(microservice_chart)
   except yaml.YAMLError as exc:
      print(exc)
   microservicename = nombre_emisor.lower() + '-jcard-restapi'
   microservice_chart_data['name'] = microservicename
   with open(microservice_chart_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(microservice_chart_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

   if external_sor == True:
      microservice_chart_yaml = 'jcard-prepaid-'+ nombre_emisor +'-ds-external-sor/Chart.yaml' 
      print('Configuring file: ' + microservice_chart_yaml) 
      microservice_chart = open(microservice_chart_yaml, 'r')
      try:
         microservice_chart_data = yaml.safe_load(microservice_chart)
      except yaml.YAMLError as exc:
         print(exc)
      microservicename = nombre_emisor.lower() + '-jcard-ds-external-sor'
      microservice_chart_data['name'] = microservicename
      with open(microservice_chart_yaml, 'w') as yaml_file:
         try:
            yaml_file.write( yaml.dump(microservice_chart_data, default_flow_style=False))
         except yaml.YAMLError as exc:
            print(exc)

   microservice_configmap_yaml = 'jcard-prepaid-'+ nombre_emisor +'-app/values-main.yaml' 
   print('Configuring file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['database']['name'] = database_emisor
   configmap_template_data['service_account'] = service_account
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)
      
   microservice_configmap_yaml = 'jcard-prepaid-'+ nombre_emisor +'-invoice/values-main.yaml' 
   print('Configuring file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['database']['name'] = database_emisor
   configmap_template_data['config']['jcard_issuer_name'] = nombre_emisor.upper()
   configmap_template_data['service_account'] = service_account
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)


   microservice_configmap_yaml = 'jcard-prepaid-'+ nombre_emisor +'-jcard/values-main.yaml' 
   print('Configuring file: ' + microservice_configmap_yaml) 
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
   if external_sor == True:
      configmap_template_data['sor']['use_internal_sor'] = "true"
      configmap_template_data['sor']['use_external_sor'] = "false"
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)
   microservice_configmap_yaml = 'jcard-prepaid-'+ nombre_emisor +'-restapi/values-main.yaml' 
   print('Configuring file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['database']['name'] = database_emisor
   configmap_template_data['configmap']['issuer_name'] = nombre_emisor.upper()
   configmap_template_data['service_account'] = service_account
   if external_sor == True:
      configmap_template_data['sor']['use_internal_sor'] = "true"
      configmap_template_data['sor']['use_external_sor'] = "false"
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

   if external_sor == True:
      microservice_configmap_yaml = 'jcard-prepaid-'+ nombre_emisor +'-ds-external-sor/values-main.yaml' 
      print('Configuring file: ' + microservice_configmap_yaml) 
      configmap_template = open(microservice_configmap_yaml, 'r')
      try:
         configmap_template_data = yaml.safe_load(configmap_template)
      except yaml.YAMLError as exc:
         print(exc)
      configmap_template_data['service_account'] = service_account
      with open(microservice_configmap_yaml, 'w') as yaml_file:
         try:
            yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
         except yaml.YAMLError as exc:
            print(exc)

   # Creo el microservicio en ArgoCD
   print('Configure Microservice in ArgoCD: ' + str(nombre_emisor) + '-jcard.yaml')
   src = '../argocd/apps/templates/jcard-prepaid-xperience-jcard.yaml'
   dest = '../argocd/apps/templates/jcard-prepaid-'+ nombre_emisor +'-jcard.yaml'
   print('Copy file: ' + src + ' to ' + dest)
   try:
      destination = shutil.copyfile(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))         
   
   microservice_configmap_yaml = dest
   print('Configuring file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['metadata']['name'] = 'jcard-prepaid-' + nombre_emisor + '-jcard'
   configmap_template_data['spec']['source']['path'] = 'apps/jcard-prepaid-' + nombre_emisor + '-jcard'
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

   print('Configure Microservice in ArgoCD: ' + str(nombre_emisor) + '-jcard.yaml')
   src = '../argocd/apps/templates/jcard-prepaid-xperience-app.yaml'
   dest = '../argocd/apps/templates/jcard-prepaid-'+ nombre_emisor +'-app.yaml'
   print('Copy file: ' + src + ' to ' + dest)
   try:
      destination = shutil.copyfile(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))  

   
   microservice_configmap_yaml = dest
   print('Configuring file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['metadata']['name'] = 'jcard-prepaid-' + nombre_emisor + '-app'
   configmap_template_data['spec']['source']['path'] = 'apps/jcard-prepaid-' + nombre_emisor + '-app'
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)     

   print('Configure Microservice in ArgoCD: ' + str(nombre_emisor) + '-invoice.yaml')
   src = '../argocd/apps/templates/jcard-prepaid-xperience-invoice.yaml'
   dest = '../argocd/apps/templates/jcard-prepaid-'+ nombre_emisor +'-invoice.yaml'
   print('Copy file: ' + src + ' to ' + dest)
   try:
      destination = shutil.copyfile(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))  

   
   microservice_configmap_yaml = dest
   print('Configuring file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['metadata']['name'] = 'jcard-prepaid-' + nombre_emisor + '-invoice'
   configmap_template_data['spec']['source']['path'] = 'apps/jcard-prepaid-' + nombre_emisor + '-invoice'
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)   

   
   print('Configure Microservice in ArgoCD: ' + str(nombre_emisor) + '-restapi.yaml')
   src = '../argocd/apps/templates/jcard-prepaid-xperience-restapi.yaml'
   dest = '../argocd/apps/templates/jcard-prepaid-'+ nombre_emisor +'-restapi.yaml'
   print('Copy file: ' + src + ' to ' + dest)
   try:
      destination = shutil.copyfile(src, dest) 
   except OSError as exc:
      print('Error copy files ' + str(exc))  

   
   microservice_configmap_yaml = dest
   print('Configuring file: ' + microservice_configmap_yaml) 
   configmap_template = open(microservice_configmap_yaml, 'r')
   try:
      configmap_template_data = yaml.safe_load(configmap_template)
   except yaml.YAMLError as exc:
      print(exc)
   configmap_template_data['metadata']['name'] = 'jcard-prepaid-' + nombre_emisor + '-restapi'
   configmap_template_data['spec']['source']['path'] = 'apps/jcard-prepaid-' + nombre_emisor + '-restapi'
   with open(microservice_configmap_yaml, 'w') as yaml_file:
      try:
         yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
      except yaml.YAMLError as exc:
         print(exc)

   if external_sor == True:
      print('Configure Microservice in ArgoCD: ' + str(nombre_emisor) + '-ds-external-sor.yaml')
      src = '../argocd/apps/templates/jcard-prepaid-xperience-restapi.yaml'
      dest = '../argocd/apps/templates/jcard-prepaid-'+ nombre_emisor +'-ds-external-sor.yaml'
      print('Copy file: ' + src + ' to ' + dest)
      try:
         destination = shutil.copyfile(src, dest) 
      except OSError as exc:
         print('Error copy files ' + str(exc))  

      
      microservice_configmap_yaml = dest
      print('Configuring file: ' + microservice_configmap_yaml) 
      configmap_template = open(microservice_configmap_yaml, 'r')
      try:
         configmap_template_data = yaml.safe_load(configmap_template)
      except yaml.YAMLError as exc:
         print(exc)
      configmap_template_data['metadata']['name'] = 'jcard-prepaid-' + nombre_emisor + '-ds-external-sor'
      configmap_template_data['spec']['source']['path'] = 'apps/jcard-prepaid-' + nombre_emisor + '-ds-external-sor'
      with open(microservice_configmap_yaml, 'w') as yaml_file:
         try:
            yaml_file.write( yaml.dump(configmap_template_data, default_flow_style=False))
         except yaml.YAMLError as exc:
            print(exc)

   
         
def Create_db():
   if create_db == True:
      # connection establishment
      conn = psycopg2.connect(
         database="postgres",
         user=DB_USER,
         password=DB_PASSWORD,
         host=DB_HOST,
         port='5432'
      )
      
      conn.autocommit = True
      
      # Creating a cursor object
      cursor = conn.cursor()
      
      # query to create a database 
      sql = 'CREATE database ' + str(database_emisor);
      
      # executing above query
      cursor.execute(sql)
      print("Database " + str(database_emisor) + " has been created successfully !!");

      # query to change owner 
      sql = 'ALTER DATABASE ' + str(database_emisor) + ' OWNER TO jpos';
      cursor.execute(sql)
      print("Change Owner db " + str(database_emisor) + " successfully !!");
      
      # Closing the connection
      conn.close()


Read_YAML()
Copy_folders()
Change_YAML()
Create_db()