#!/usr/bin/env python
import argparse
import scapy.all as scapy

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_brodcast = brodcast / arp_request
    # the scap.srp() functionn return two lists the answered list and the unanswered list
    answered_list = scapy.srp(arp_request_brodcast, timeout=1, verbose=False)[0]

    client_list = []
    for i in answered_list:
        client_dictionary = {"ip": i[1].psrc, "mac": i[1].hwsrc}
        client_list.append(client_dictionary)
    return client_list

def print_result(resuls_list):
    print("IP\t\t\t\tMAC ADDRESS\n--------------------------------------------------")
    for client in resuls_list:
        print(client["ip"] + "\t\t\t" + client["mac"])


options = get_arguments()
Scan_result = scan(options.target)
print_result(Scan_result)