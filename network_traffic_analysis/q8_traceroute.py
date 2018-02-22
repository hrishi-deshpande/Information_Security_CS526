#Identify host(s) attempting a directory traversal.
import pyshark

#Input the trace file
#The filter is meant to accept packets for the udp protocol with no application layer payload
#Essentially, protocols like DNS also use UDP as a transport level protocol but we don't want to consider these packets.
#Since traceroute uses UDP but does not use any transport level packets, want only those packets that use udp as a transport
#but with not application layer payload.
trace_input = pyshark.FileCapture("project2.trace", display_filter='udp and not dns and not browser and not mdns and not cups and not nbns and not auto_rp and not smb_netlogon')

#declare an Empty dictionary. This structure will store the IP addresses of the source host and destination hosts
ip_dict = {}

#Now iterate over the packets from the trace_input.
#We extract the source IP address and build a Dictionary whose each tuple if of the form (<source_ip>, <destination_ip>):<list_of_ttl_values>
#Here the key is a UDP connection endpoint (<source_ip>, <destination_ip) while the value is a list of all ttl values.
for packet in trace_input:
			   ip_src = packet.ip.src
			   ip_dst = packet.ip.dst
			   #Get the IP endpoints for the trace route.
			   ip_endpoints = (ip_src, ip_dst)
			   ttl_dict = set()
			   if ip_endpoints in ip_dict:
				   ttl_dict = ip_dict[ip_endpoints]
				   ttl = int(packet.ip.ttl)
				   if ttl not in ttl_dict:
					   ttl_dict.add(ttl)
			   else:
				   ttl_dict.add(int(packet.ip.ttl))
                           #Store the ttl value in the dictionary
			   ip_dict[ip_endpoints] = ttl_dict

print("Printing the whole structure:")
print(ip_dict)

#Clearly, there's some host <source_ip, dest_ip> pair with increasing ttl values.
#So the source_ip is our required source that's attempting a traceroute.
print("\nMalicious host and its target:")
for endpoint in ip_dict:
    if len(ip_dict[endpoint]) > 1:
        print (endpoint)
