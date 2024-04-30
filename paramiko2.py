#/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler
from time import time
from jinja2 import Environment, FileSystemLoader

ip_addr = input("Enter IP address: ")

device = {
	'device_type': 'cisco_ios',
	'ip': ip_addr,
	'username': 'root',
	'password': getpass(),
	'port':22,
}

net_connect = ConnectHandler(**device)

commands = [
    'interface FastEthernet 0/2',
    'description configured by netmiko',
    'switchport access vlan 20'
]

output = net_connect.send_config_set(commands)

print(output)