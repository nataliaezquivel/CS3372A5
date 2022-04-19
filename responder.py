#!/usr/bin/env python3

#**************************************************************
# Natalia Ezquivel
# Lab 5 - April 18 2022
# CS3372
#**************************************************************

import scapy.all as scapy

def main():
    print("ICMP Echo Request Responder using scapy...")

    print("Sending a ping ICMP echo request...")
    request = scapy.IP()/scapy.ICMP(id=1,seq=1)
    scapy.send( request )
    print("Request...")
    print("Source:", request.src)
    print("Destination:", request.dst)
    
    #print("Sniffing for a ping ICMP echo request...")
    #sniff_ = scapy.sniff(filter="src 127.0.0.1 and dst 127.0.0.1", count=2,iface='lo')
    #print("Done sniffing...")
    #if sniff_ is not None:
    #    print(sniff_)
    #    sniff_.summary()
    #    print("----------")
    #    print(sniff_[1])
    #    sniff_[1].display()
    #    print("----------")
    #    icmp = sniff_[1].getlayer('ICMP')
    #    icmp.display()

    print("Responding the ping ICMP echo request...")
    scapy.send(scapy.IP(dst="127.0.0.1",src="127.0.0.1")/scapy.ICMP())
    reply = scapy.sr1(scapy.IP()/scapy.ICMP(id=1,seq=1,length=64),timeout=3)
    if reply is not None:
        print("Reply...")
        print("Source:",reply.src)
        print("Destination:",reply.dst)


if __name__ == "__main__":
    main()


