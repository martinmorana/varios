import yaml

with open("data.yaml") as f:
     list_doc = yaml.safe_load(f)

for sense in list_doc:
    if sense["name"] == "sense2":
         sense["value"] = 1234

with open("data.yaml", "w") as f:
    yaml.dump(list_doc, f)