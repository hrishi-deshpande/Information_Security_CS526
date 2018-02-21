#Identify host(s) attempting a reflected cross-side scripting attack
import pyshark

#Next read the input trace file.
#We need to filter out only those packets that use http as the application layer protocol.
#Also, since we are looking for hosts that attempt a reflected xss attack, we only check for http hosts that send <script> </script> tags
#in their url during the http requests
input_trace = pyshark.FileCapture("project2.trace", display_filter='http and  http.request.uri contains "<script>"  and http.request.uri contains "</script"')

#Create an empty set that will hold info about hosts  that attempt a reflected XSS attack and the attack target.
src_ip_set = set()

#Now iterate over the filtered packets and collect the IP addresses of the hosts involved in the XSS attack.
for packet in input_trace:
	src_ip_set.add((packet.ip.src, packet.ip.dst))

#The printed output contains IP address of the malicious host and the attack target.
print(src_ip_set)



