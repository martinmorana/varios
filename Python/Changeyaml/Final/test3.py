from ctypes.wintypes import PINT
import yaml
import os
# /usr/bin/python3 test3.py

AMBIENTE = os.getenv('AMBIENTE')
print('el entorno es ' + AMBIENTE)


def read_values():
   with open('config.yaml') as yaml_config:
      configmap_input = yaml.safe_load(yaml_config)
      #print(data)
   test = configmap_input[AMBIENTE]['configmap']['data']

   
   stream = open('output.yaml', 'r')
   data = yaml.safe_load(stream)
   #configmap_output = data['configmap']['data']

   for configmap in test:
         print(configmap)
         print(test[configmap])
         #configmap_output[configmap] = test[configmap]
         data['configmap']['data'][configmap] = test[configmap]
         print(data)

   print(data)

   with open('output.yaml', 'w') as yaml_file:
    yaml_file.write( yaml.dump(data, default_flow_style=False))
 


  
   


      
read_values()

#write_values()
#test.update(dict(variable1=11, variable2=22))


""" with open('values-main.yaml') as f:
    doc = yaml.load(f)
    # values = doc['components']['star']['init'][0]['values2']
    # values['logg'] = "pwee"
    # with open(f'config-2.yaml', 'w') as out:
    #     yaml.dump(doc, out)
    values = doc['configmap']['data']
    values['variable1'] = "pwee"
    values['variable2'] = "pwee"
    with open(f'values-main.yaml', 'w') as out:
        yaml.dump(doc, out) """
  