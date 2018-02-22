#Identify the TCP endpoint with the broadest coverage in their Initial Sequence Number Used.
import pyshark

#Read the input trace file. For Initial Sequence numbers we need to check that syn = 1 and ack = 0.
#This is because that packet will be the 1st packet sent from the src to dest.
#So its sequence number 
input_trace = pyshark.FileCapture("project2.trace", display_filter='tcp and tcp.flags.syn == 1 and tcp.flags.ack == 0')

tcp_endpoint_dict = {}

for packets in input_trace:
        src_ip = packets.ip.src
        dst_ip = packets.ip.dst
        seqno = int(packets.tcp.seq)
        seqno_set = set()
        endpoint = (src_ip, dst_ip)
        if endpoint in tcp_endpoint_dict:
                seqno_set = tcp_endpoint_dict[endpoint]
        seqno_set.add(seqno)
        tcp_endpoint_dict[endpoint] = seqno_set


my_endpoint = ()
max_diff = 0
for endpoint in tcp_endpoint_dict:
        seqno_set = tcp_endpoint_dict[endpoint]
        seqno_list = list(seqno_set)
        
        diff = max(seqno_set) - min(seqno_set)
        if (len(seqno_list) >= 5 and diff > max_diff):
                max_diff = diff
                my_endpoint = endpoint

print (my_endpoint)




        
        
                        
