import json
print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
with open('json_sample.json', 'r') as file:
        g = json.load(file)
        for gg in g['imdata']:
                print(gg["l1PhysIf"]['attributes']['dn'], '                             ', gg["l1PhysIf"]['attributes']['fecMode'], '', gg["l1PhysIf"]['attributes']['mtu'])