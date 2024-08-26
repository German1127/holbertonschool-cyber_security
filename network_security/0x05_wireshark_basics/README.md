0. IP protocol scan
Create a Wireshark filter to detect packets sent by the nmap -sO <target> command for IP protocol scanning.

ip.proto == 1

ip:
This refers to the IP (Internet Protocol) protocol. It is a general category in Wireshark that is used to filter IP-related packets.

proto:
It is an abbreviation of "protocol" (protocol). Within the context of the IP filter, proto indicates the field that specifies the protocol that is encapsulated in the IP packet.

==:
This is the comparison operator in Wireshark. Used to check if the value of a field is equal to the specified value.

1:
This is the number that represents the ICMP protocol in the proto field of the IP header. Each protocol at the network layer is assigned a number, and 1 is the number for ICMP.

======

1. TCP SYN scan
Create a Wireshark filter to detect packets sent by the nmap -sS <target> command for TCP SYN scan.

tcp.flags.syn == 1 and ip.dst == 10.42.68.80  and tcp.window_size <= 1024 andtcp.flags.ack == 0 

tcp.flags.syn == 1:
This filter selects TCP packets where the SYN (synchronize) bit is set. The SYN bit is used to start a TCP connection, so this filter selects starting packets from a TCP connection.

ip.dst == 10.42.68.80:
This filter selects IP packets whose destination is the IP address 10.42.68.80. Limits the search to packages that are sent to that specific address.

tcp.window_size <= 1024:
This filter selects TCP packets in which the TCP window size is less than or equal to 1024 bytes. The TCP window size indicates the amount of data the receiver is willing to accept before an acknowledgment is required.

tcp.flags.ack == 0:
This filter selects TCP packets where the ACK (acknowledgment) bit is disabled. The ACK bit is used to acknowledge receipt of data on a TCP connection, so this filter selects packets that are not acknowledging receipt of data.

======

2. TCP Connect() scan
Create a Wireshark filter to detect packets sent by the nmap -sT <target> command for TCP Connect() scan.

tcp.flags.syn == 1 and tcp.flags.ack == 0 and tcp.window_size > 1024

tcp.flags.syn == 1:
This filter selects TCP packets in which the SYN (synchronize) bit is set. The SYN bit is used to initiate a TCP connection, so this filter looks for packets that are trying to establish a new connection.

tcp.flags.ack == 0:
This filter selects TCP packets in which the ACK (acknowledgment) bit is disabled. The ACK bit is used to confirm receipt of data on a TCP connection, so this filter looks for packets that are not acknowledging receipt of data.

tcp.window_size > 1024:
This filter selects TCP packets in which the TCP window size is greater than 1024 bytes. The TCP window size indicates how much data the receiver is willing to accept before needing an acknowledgment.

======

3. TCP FIN scan
Create a Wireshark filter to detect packets sent by the nmap -sF <target> command for TCP FIN scan .

tcp.flags.fin == 1 and tcp.flags.ack == 0 and tcp.flags.syn == 0 and tcp.flags == 0x001

tcp.flags.fin == 1:
This filter selects TCP packets in which the FIN bit is set. The FIN bit is used to terminate a TCP connection.

tcp.flags.ack == 0:
This filter selects TCP packets in which the ACK (acknowledgment) bit is set to off. The ACK bit is used to confirm receipt of data, so this filter selects packets that are not acknowledging receipt of data.

tcp.flags.syn == 0:
This filter selects TCP packets in which the SYN (synchronize) bit is disabled. The SYN bit is used to start a TCP connection, so this filter excludes packets that are trying to start a new connection.

tcp.flags == 0x001:
This filter selects TCP packets whose flags field is set to exactly 0x001 in hexadecimal notation. In binary, this corresponds to 0000 0001, meaning that only the FIN bit is set. This is a direct way to search for packets where the only flag set is FIN.

======

4. TCP ping sweeps
Create a Wireshark filter to detect packets sent by the nmap -sn -PS/-PA <subnet> command for TCP SYN Ping/TCP ACK Ping .

(tcp.flags.syn == 1 and tcp.flags.ack == 0) or (tcp.flags.ack == 1 and tcp.flags.syn == 0)

tcp.flags.syn == 1:
This filter selects TCP packets where the SYN (synchronize) bit is set. This bit is used to start a new TCP connection.

tcp.flags.ack == 0:
This filter selects TCP packets where the ACK (acknowledgment) bit is disabled. The ACK bit is used to confirm receipt of data.

======

5. UDP port scan
Create a Wireshark filter to detect packets sent by the nmap -sU <target> command for UDP port scan .

icmp.type == 3 and icmp.code == 3

icmp.type == 3:

icmp.type == 3:

ICMP Type 3:
This filter selects ICMP packets whose type is 3. In the ICMP protocol, type 3 indicates a Destination Unreachable message. This means that the IP packet could not be delivered to the destination.
icmp.code == 3:

ICMP Code 3:
Within type 3, code 3 specifies Port Unreachable. This indicates that the port to which the packet was attempted to be sent at the destination is not available. It is a common response when the destination is available, but the specific port is not listening.

======

6. UDP ping sweeps
Create a Wireshark filter to detect packets sent by the nmap -sn -PU <subnet> command for UDP ping sweeps .

udp.dstport == 7

udp.dstport == 7:
in Wireshark is used to select and display UDP (User Datagram Protocol) packets whose destination port is 7.

======

7. ICMP ping sweep
Create a Wireshark filter to detect packets sent by the nmap -sn -PE <subnet> command for ICMP ping sweeps .

icmp.type == 8 or icmp.type == 0

icmp.type == 8:

ICMP Type 8:
Selects ICMP packets where the type is 8. This type corresponds to Echo Request. It is a message sent to request an echo response, commonly used by the ping command to verify network connectivity.
icmp.type == 0:

ICMP Type 0:
Selects ICMP packets where the type is 0. This type corresponds to Echo Reply. It is the response to the Echo Request message, indicating that the destination host received the message and is responding.

======

8. ARP scanning
Create a Wireshark filter to detect packets sent by the arp-scan -l command for ARP scanning .

arp:
Refers to the ARP protocol, which is used to map IP addresses to MAC addresses on a local network.

dst.hw_mac:
This is an abbreviation for "destination hardware MAC address". In ARP, this is the MAC address to which the ARP packet is directed.

== 00:00:00:00:00:00:
This is the value being searched for in the destination MAC address field. 00:00:00:00:00:00 is a MAC address that, in most cases, is used to represent an unassigned MAC address or a "broadcast" MAC address when information is being requested.
