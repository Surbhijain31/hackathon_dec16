#importing json and os packages
import json
import os

filename = 'sample.json'

#opening json file in read mode
with open(filename, 'r') as f:

    #Loading json into a variable
    data = json.load(f)

    #Changing firewall - protocol - from tcp to udp
    data['featureConfigs']['features'][2]['firewallRules']['firewallRules'][0]['application']['service'][0]['protocol']='udp'

    #Changeing 3rd vnics- portgroup name to EXT_VLAN_201b
    data['vnics']['vnics'][2]['postgroupName']="EXT_VLAN_201b"
    
    #Changing ospf- enabled = false to true 
    data['featureConfigs']['features'][5]['ospf']['enabled']="true"

    #Updating holddowntimer = holddowntimer +keepalivetimer
    holddowntimer = data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][0]['holdDownTimer']
    keepalivetimer = data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][0]['keepAliveTimer']
    holddowntimer=holddowntimer+keepalivetimer
    data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][0]['holdDownTimer']=holddowntimer

    holddowntimer = data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][1]['holdDownTimer']
    keepalivetimer= data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][1]['keepAliveTimer']
    holddowntimer=holddowntimer+keepalivetimer
    data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][1]['holdDownTimer']=holddowntimer

    holddowntimer = data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][2]['holdDownTimer']
    keepalivetimer = data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][2]['keepAliveTimer']
    holddowntimer=holddowntimer+keepalivetimer
    data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][2]['holdDownTimer']=holddowntimer
    
#Removing file    
os.remove(filename)

#Opening file in write mode and dumping updated json data
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)
