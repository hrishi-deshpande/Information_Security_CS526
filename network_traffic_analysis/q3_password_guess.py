#Password Guessing

import pyshark

#We need to determine the host that is attempting password guessing on a secure ftp server.
#For this we check the failed login attempts. For failed logins, ftp returns a status code of 530.
input_trace = pyshark.FileCapture("project2.trace", display_filter='ftp and ftp.response.code == 530')

#Declare an empty set. we use this store the list of malicious host IP's.
malicious_host_ip = {}

#iterate over the packets and check for potentially malicious host IP's that repeated failed login attempts.
for packet in input_trace:
	src_ip = packet.ip.src
	if src_ip in malicious_host_ip:
		malicious_host_ip[src_ip] = malicious_host_ip[src_ip] + 1
	else:
		malicious_host_ip[src_ip] = 1

print("Potentially malicious Host(s):")

#A single failed login attempt can be expected. Multiple failed login attempts raise suspicion of a malicious host.
for key in malicious_host_ip:
	if malicious_host_ip[key] > 0:
		print (key)

