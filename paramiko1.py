#/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

ip_addr = input("Enter IP address: ")

device = {
	'device_type': 'cisco_ios',
	'ip': ip_addr,
	'username': 'root',
	'password': getpass(),
	'port':22,
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command_expect("show version")

print()
print('#' * 50)
print(output)
print('#' * 50)
print()