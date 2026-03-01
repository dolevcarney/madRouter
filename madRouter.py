from scapy.all import *
import ipaddress

sniffed_iface = 'enp0s3'
routing_table = [('192.168.0.0/24','enp0s3'), ('192.168.56.0/24','enp0s8')]

def send_packet(packet):
    iface_to_send = [iface for ip,iface in routing_table if ipaddress.ip_address(packet[IP].dst) in ipaddress.ip_network(ip)]
    if((len(iface_to_send) != 0) and (iface_to_send[0] != sniffed_iface)):
        sendp(packet, iface=iface_to_send[0])


def main():
    sniff(iface=sniffed_iface ,lfilter= lambda p: p.haslayer(IP),prn=lambda pkt: send_packet(pkt))

if __name__ == "__main__":
    main()