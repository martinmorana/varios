from ctypes.wintypes import PINT
import yaml
import os
# /usr/bin/python3 test3.py

AMBIENTE = os.getenv('AMBIENTE')
print(AMBIENTE)


def read_values():
   with open('config.yaml') as yaml_config:
      configmap_input = yaml.safe_load(yaml_config)
      #print(data)
   test = configmap_input[AMBIENTE]['configmap']['data']
   print(test['variable1'])
   for configmap in test:
        print(configmap)
        print(test[configmap])

   with open('output.yaml') as yaml_output:
      data = yaml.safe_load(yaml_output)
      #print(data)
  
   


      
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
  