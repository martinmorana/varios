from ctypes.wintypes import PINT
import yaml
import os
# /usr/bin/python3 test3.py

AMBIENTE = os.getenv('AMBIENTE')
print(AMBIENTE)


def read_values():
   with open('config.yaml') as stream:
      data = yaml.safe_load(stream)
      #print(data)
   test = data[AMBIENTE]['configmap']['data']
   print(test)
  

def write_values():
 
   with open('output.yaml') as stream2:
      configmap = yaml.safe_load(stream2)
      configmap2 = configmap['configmap']['data']
      #configmap.update(test)
      print(configmap2)
      configmap2 = ['configmap']['data']
   #with open('output.yaml', "w") as stream2:   
      #yaml.safe_dump(configmap, stream2, default_flow_style=False, explicit_start=False, allow_unicode=True, encoding='utf-8')
      #yaml.dump(test, stream2)

read_values()
write_values()
#test.update(dict(variable1=11, variable2=22))

  