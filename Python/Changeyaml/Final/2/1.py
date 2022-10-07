#!/usr/bin/env python

import yaml

with open("testfile.yaml", 'r') as stream:
    try:
        loaded = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Modify the fields from the dict
loaded['test']['name'] = "Max"
loaded['test']['age'] = "10"
loaded['test']['version'] = "2.2"

# Save it again
with open("modified.yaml", 'w') as stream:
    try:
        yaml.dump(loaded, stream, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)