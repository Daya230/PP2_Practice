import json

with open("json_s.json","r") as f:
    data = json.load(f)
"""print("Interface Status")
print("================================================================================")
print(f"{'DN':50} {'Description':20} {'Speed':5} {'MTU':5}")
print("-"*50, "-"*20, "-"*5, "-"*5)"""
print(
    """
Interface Status
=======================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
    """
)
for x in data["imdata"]:
    att = x["l1PhysIf"]["attributes"]
    dn = att.get("dn", "")
    descr = att.get("descr","")
    speed = att.get("speed", "")
    mtu = att.get("mtu", "")
    print(f"{dn:50} {descr:20} {speed:5}   {mtu:6}")