from ctypes.wintypes import PINT
import yaml
import os

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
      #configmap = configmap['configmap']['data']
      print(configmap)
      configmap.update(test)
      print(configmap)
   with open('output.yaml', "w") as stream2:   
      yaml.safe_dump(configmap, stream2, default_flow_style=False, explicit_start=False, allow_unicode=True, encoding='utf-8')
      #yaml.dump(configmap, stream2)

read_values()
#test.update(dict(variable1=11, variable2=22))

  