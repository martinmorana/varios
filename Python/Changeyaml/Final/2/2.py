import yaml

fname = "some.yaml"

stream = open(fname, 'r')
data = yaml.safe_load(stream)

data['instances'][0]['host'] = '1.2.3.4'
data['instances'][0]['username'] = 'Username'
data['instances'][0]['password'] = 'Password'

with open(fname, 'w') as yaml_file:
    yaml_file.write( yaml.dump(data, default_flow_style=False))