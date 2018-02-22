#Find the Apache Server that runs the oldest version.
import pyshark
from packaging import version
from functools import cmp_to_key

def cmp_versions(a, b):
	if (version.parse(a) < version.parse(b)):
		return -1
	elif (version.parse(b) < version.parse(b)):
		return 0
		
	return 1

#Filter out http traffic that uses an Apache HTTP web server.
input_trace = pyshark.FileCapture("project2.trace", display_filter='http and http.server contains "Apache/"')

#Create an empty dictionary. Key: Apache Version and Value:List of servers with that version.
server_version = {}

#Now iterate over packets and store IP's addresses of servers and the current version of Apache that they're running.
for packets in input_trace:
	#Extract server version from the input packet
	server = packets.http.server
	server_arr = server.split(' ')
	server = server_arr[0]
	server = server.replace('Apache/', '')
	
	#extract source ip from the input packet
	src_ip = packets.ip.src 
	src_ip_set = set()
	
	#Check if the given version is already in the map. If yes, then simply append the IP address.
	if server in server_version:
		src_ip_set = server_version[server]
	
	src_ip_set.add(src_ip)
	server_version[server] = src_ip_set


#Extract versions from the dictionary and sort the list of versions.
versionList = [*server_version]
versionList.sort(key=cmp_to_key(cmp_versions))

#Print the server(s) with the oldest version which is the first element in the sorted list.
print(versionList[0], ":", server_version[versionList[0]])

