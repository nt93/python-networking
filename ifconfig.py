import os
import subprocess
import re


p = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)

output = str(p.communicate())
#print (type(ip))

#ifconfig = check_out([ifconfig])

#print(type(ifconfig))
ip = re.compile(r'\b\d+(?:\.\d+){3}\b', re.MULTILINE)

ip_list = '\t'.join(re.findall(ip, output))

print("IPs list: " ,ip_list)