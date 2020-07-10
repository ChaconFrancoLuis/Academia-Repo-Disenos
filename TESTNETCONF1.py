from ncclient import manager
from demo1 import Ios_device

device_manager = manager.connect(
    host = Ios_device["address"],
    port = Ios_device["netconf_port"],
    username = Ios_device["username"],
    password = Ios_device["password"],
    hostkey_verify = False)



netconf_reply = device_manager.get_config(source = "running")
print(netconf_reply)
