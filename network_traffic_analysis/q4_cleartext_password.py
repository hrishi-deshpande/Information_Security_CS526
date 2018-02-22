import pyshark

#For this problem, we can only partially automate the process.
#Since there's no perfect way to know whether any password was sent in clear text or not.
#Clear text passwords will be verified by manual inspection.
input_trace = pyshark.FileCapture("project2.trace", display_filter='ftp or http or telnet or pop')

#Empty set to hold tcp streams.
tcp_streams = set()

for packets in input_trace:
	tcp_streams.add(int(packets.tcp.stream))
	
#We will print out a list of tcp streams for protocols ftp, telnet, http and pop and then examine them manually via wireshark GUI.
print("List of tcp streams to examine manually for clear text passwords:")
print(sorted(tcp_streams))



