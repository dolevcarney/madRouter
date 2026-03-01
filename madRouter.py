from scapy.all import *

def main():
    sniff(iface='enp0s8' ,prn=lambda x: sendp(x,iface='enp0s9'))

if __name__ == "__main__":
    main()
