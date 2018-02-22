#Identify a list of all HTTP servers.
import pyshark

#First read the input trace file. We need to obtain those packets that have http as the application protocol
#and for whom the http response was properly returned back to the client. 
input_trace = pyshark.FileCapture("project2.trace", display_filter='http and http.response.code != 0')

#Create a set of IP addresses of the http servers involved in a valid HTTP exchange.
#A set can only have unique IP addresses.
http_server_set = set()

#First input the file. 
for packet in input_trace:
	http_server_set.add(packet.ip.src)

#Next print out the set contents
print(sorted(http_server_set))

print(len(http_server_set))
