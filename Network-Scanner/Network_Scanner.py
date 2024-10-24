import argparse
from scapy.all import *
import socket

def arp_scan(ip):
    """
    Performs a network scan by sending ARP requests to an IP address or a range of IP addresses.

    Args:
        ip (str): An IP address or IP address range to scan. For example:
                    - 192.168.1.1 to scan a single IP address
                    - 192.168.1.1/24 to scan a range of IP addresses.

    Returns:
        A list of dictionaries mapping IP addresses to MAC addresses. For example:
        [
            {'IP': '192.168.2.1', 'MAC': 'c4:93:d9:8b:3e:5a'}
        ]
    """
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    ans, _ = srp(request, timeout=2, retry=1, verbose=False)
    return [{'IP': received.psrc, 'MAC': received.hwsrc} for sent, received in ans]



def tcp_scan(ip, ports):
    """
    Performs a TCP scan by sending SYN packets to <ports>.

    Args:
        ip (str): An IP address or hostname to target.
        ports (list or tuple of int): A list or tuple of ports to scan.

    Returns:
        A list of ports that are open.
    """
    if isinstance(ports, tuple):
        ports = list(range(ports[0], ports[1] + 1))
    syn_packets = IP(dst=ip) / TCP(dport=ports, flags="S")
    ans, _ = sr(syn_packets, timeout=2, retry=1, verbose=False)
    return [received[TCP].sport for sent, received in ans if received[TCP].flags == "SA"]

def udp_scan(ip, ports):
    if isinstance(ports, tuple):
        ports = list(range(ports[0], ports[1] + 1))
    udp_packets = IP(dst=ip) / UDP(dport=ports)
    ans, unans = sr(udp_packets, timeout=2, retry=1, verbose=False)
    result = [{'Port': received[UDP].sport, 'State': 'Open'} for sent, received in ans]
    for sent in unans:
        result.append({'Port': sent[UDP].dport, 'State': 'Closed/Filtered'})
    return result

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", help="Command to perform.", required=True)

    arp_subparser = subparsers.add_parser('ARP', help='Perform a network scan using ARP requests.')
    arp_subparser.add_argument('IP', help='An IP address (e.g. 192.168.1.1) or range (e.g. 192.168.1.1/24).')

    tcp_subparser = subparsers.add_parser('TCP', help='Perform a TCP scan using SYN packets.')
    tcp_subparser.add_argument('IP', help='An IP address or hostname to target.')
    tcp_subparser.add_argument('ports', nargs='+', type=int, help='Ports to scan.')
    tcp_subparser.add_argument('--range', action='store_true', help='Scan a range of ports.')

    udp_subparser = subparsers.add_parser('UDP', help='Perform a UDP scan.')
    udp_subparser.add_argument('IP', help='An IP address or hostname to target.')
    udp_subparser.add_argument('ports', nargs='+', type=int, help='Ports to scan.')
    udp_subparser.add_argument('--range', action='store_true', help='Scan a range of ports.')

    args = parser.parse_args()

    if args.command == 'ARP':
        result = arp_scan(args.IP)
        for mapping in result:
            print(f'{mapping["IP"]} ==> {mapping["MAC"]}')

    elif args.command == 'TCP':
        ports = tuple(args.ports) if args.range else args.ports
        result = tcp_scan(args.IP, ports)
        for port in result:
            print(f'Port {port} is open.')

    elif args.command == 'UDP':
        ports = tuple(args.ports) if args.range else args.ports
        result = udp_scan(args.IP, ports)
        for res in result:
            print(f'Port {res["Port"]} is {res["State"]}')

if __name__ == '__main__':
    main()