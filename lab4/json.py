import json
print('Interface Status')
print('================================================================================')
print('DN                                  x.                Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
with open('json_sample.json','r') as file:
    save = json.load(file)
    for gg in save['imdata']:
        print(gg["l1PhysIf"]["attributes"]["dn"],'                              ', gg["l1PhysIf"]["attributes"]["fecMode"],'   ',gg["l1PhysIf"]["attributes"]["mtu"])