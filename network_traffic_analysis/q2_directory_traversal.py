#Find hosts attempting a Directory Traversal
import pyshark

#First read the input source file.
#Next we want to filter out only those packets that use http as the application protocol
#and out of these packets we further filter out only those http requests where the host attempts a directory traversal.
input_trace = pyshark.FileCapture("project2.trace", display_filter='http and http.request.uri contains "../.."')

#Create an empty set
src_host = set()

#Next we iterate over these packets and store the source IP address of all source hosts attempting a directory traversal.
for packet in input_trace:
	src_host.add(packet.ip.src)
	
print(sorted(src_host))


