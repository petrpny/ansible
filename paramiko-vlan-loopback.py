import paramiko
import time

router_ip = "192.168.1.121"
router_username = "root"
router_password = "PhilipsR00t!"

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(router_ip, 
            username=router_username, 
            password=router_password,
            look_for_keys=False )
            
print("Successful connection", router_ip)

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("int loop 0\n")
remote_connection.send("ip address 1.1.1.1 255.255.255.255\n")
remote_connection.send("int loop 1\n")
remote_connection.send("ip address 2.2.2.2 255.255.255.255\n")
remote_connection.send("router ospf 1\n")
remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n")

for n in range (2,21):
    print("Creating VLAN " + str(n))
    remote_connection.send("vlan " + str(n) +  "\n")
    remote_connection.send("name Python_VLAN_" + str(n) +  "\n")
    time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print(output)

ssh_client.close