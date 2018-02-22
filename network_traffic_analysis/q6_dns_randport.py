import pyshark

#We need to look for hosts making dns requests and whether the hosts use random port no's or not.
input_trace = pyshark.FileCapture("project2.trace", display_filter='dns && dns.flags.response == 0')

#Create an dictionary for host IP's and the port numbers they use for DNS queries.
host_ips = {}

#Iterate over the filtered packets and extract the source IP and port numbers for each DNS request.
for packets in input_trace:
	src_ip = packets.ip.src
	src_port = packets.udp.srcport
	port_set = set()

	#Check if IP is already in Dictionary. If yes, then simply append the source port number to the existing list.
	if src_ip in host_ips:
		port_set = host_ips[src_ip]
	port_set.add(src_port)
	host_ips[src_ip] = port_set

#Check if the host has only once src port number used for dns. This means that it is not using random port numbers.
suspicious_hosts = set()
for key in host_ips:
	if (len(host_ips[key]) == 1):
		suspicious_hosts.add(key)
		
#Print the list of suspicious hosts. For the given trace, there are exactly 2 such hosts.
print(sorted(suspicious_hosts))

	


	
	
