#Identify the TCP endpoint with the broadest coverage in their Initial Sequence Number Used.
import pyshark

#Read the input trace file. For Initial Sequence numbers we need to check that syn = 1 and ack = 0.
#This is because that packet will be the 1st packet sent from the src to dest.
#So its sequence number will be the inital sequence number (ISN).
input_trace = pyshark.FileCapture("project2.trace", display_filter='tcp and tcp.flags.syn == 1 and tcp.flags.ack == 0')

#Create a dictionary to store tcp endpoints and a list of tcp sequence numbers.
tcp_endpoint_dict = {}

#Iterate over the packets in the input trace file.
for packets in input_trace:
		#extract the source and destination IP addresses for the given TCP endpoint.
        src_ip = packets.ip.src
        dst_ip = packets.ip.dst
		#Also note the initial sequence number.
        seqno = int(packets.tcp.seq)
        seqno_set = set()
		
		#Check if the given endpoint is already in the dictionary. In that case, just append the extracted ISN.
        endpoint = (src_ip, dst_ip)
        if endpoint in tcp_endpoint_dict:
                seqno_set = tcp_endpoint_dict[endpoint]
        seqno_set.add(seqno)
        tcp_endpoint_dict[endpoint] = seqno_set


#Compute the TCP endpoints with the max coverage.
my_endpoint = ()
max_diff = 0
for endpoint in tcp_endpoint_dict:
        seqno_set = tcp_endpoint_dict[endpoint]
        seqno_list = list(seqno_set)
        
		#Obtain the coverage for the given endpoint
        diff = max(seqno_set) - min(seqno_set)
        if (len(seqno_list) >= 5 and diff > max_diff):
                max_diff = diff
                my_endpoint = endpoint

#Print the endpoint with the maximum coverage.
print("TCP endpoint with the broadest coverage")
print (my_endpoint)




        
        
                        
