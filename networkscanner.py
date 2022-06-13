import scapy.all as scapy
import optparse

def scan_network(ip):
    arp_request_packet = scapy.ARP(pdst = ip)
    broadcast_packet = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout = 1)
    answered_list.summary()

def get_inputs():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--ip', dest = 'ip', help = 'Enter a IP Address')
    (inputs, arguments) = parser.parse_args()
    if not inputs.ip:
        print('Enter a IP Address')
    return inputs

print('networkscanner has been launced')
inputs = get_inputs()

scan_network(inputs.ip)












