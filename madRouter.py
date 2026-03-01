from scapy.all import *

sniffed_iface = 'enp0s3'
routing_table = [('192.168.0','enp0s3'), ('192.168.56','enp0s8')]

def send_packet(packet):
    send_to = [(ip,iface) for ip,iface in routing_table if packet[IP].dst.startswith(ip)]
    if((len(send_to) != 0) and (send_to[0][1] != sniffed_iface)):
        sendp(packet, iface=send_to[0][1])


def main():
    sniff(iface=sniffed_iface ,lfilter= lambda p: p.haslayer(IP),prn=lambda pkt: send_packet(pkt))

if __name__ == "__main__":
    main()