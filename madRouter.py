from scapy.all import *
import ipaddress
import socket
import select 

routing_table = [('192.168.0.1/24',2), ('192.168.56.0/24',3),("192.168.1.2/24",2)]
iface1 = 'enp0s3'
iface2 = 'enp0s8'
ETH_P_IP = 0x800
MAX_PACKET_SIZE = 1535
ELIS_IP = '192.168.1.2'
ELIS_MAC = 'bb:bb:bb:bb:bb:bb'
PROXY_MAC = 'aa:aa:aa:aa:aa:aa'
PROXY_IP = '1.1.1.1'

def send_packet(packet):
    iface_to_send = [iface for ip, iface in routing_table if ipaddress.ip_address(packet[IP].dst) in ipaddress.ip_network(ip)]
    if(len(iface_to_send)!=0  and iface_to_send[0] != sniffed_iface):
        sendp(packet, iface=iface_to_send)
 
 
def main():
	in_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_IP))
	out_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_IP))
	
	in_socket.setblocking(False)
	out_socket.setblocking(False)

	in_socket.bind((IN_IFACE_IP, 0))
	out_socket.bind((OUT_IFACE_IP, 0))

	while(True):
		readable, _, _ = select.select([s1, s2], [], [])
		for sock in readable:
			packet = sock.recv(MAX_PACKET_SIZE)
			scapy_packet = Ether(packet)
			if sock == in_socket:
				scapy_packet[IP].src = PROXY_IP
				scapy_packet[Ether].source = PROXY_MAC
			else:
				scapy_packet[IP].dst = ELIS_IP
				scapy_packet[MAC].dest = ELIS.MAC
			send_packet(scapy_packet)
	
 
if __name__ == "__main__":
    main()
