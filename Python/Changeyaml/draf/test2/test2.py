from csv import reader
import yaml


with open('values-main.yaml') as f:
    doc = yaml.load(f)
    # values = doc['components']['star']['init'][0]['values2']
    # values['logg'] = "pwee"
    # with open(f'config-2.yaml', 'w') as out:
    #     yaml.dump(doc, out)
    values = doc['configmap']['data']
    values['variable1'] = "pwee"
    values['variable2'] = "pwee"
    with open(f'values-main.yaml', 'w') as out:
        yaml.dump(doc, out)



