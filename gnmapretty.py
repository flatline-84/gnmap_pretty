#!/usr/bin/env python3

import os
import sys
import argparse
import re
from colorama import init, deinit
from colorama import Fore, Back, Style

re_host = r'(Host: )(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

def main(arguments):

    # Argparser initialization
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input .gnmap file to be parsed")

    args = parser.parse_args(arguments)

    rfile = open(args.infile, "rt")
    # print(rfile)

    host = {}
    ## Parse the file here.
    content = rfile.readlines()
    for line in content:
        # NMAP Version, Scan Time
        if len(re.findall(r'(scan initiated)', line)):
            host['nmap_version'] = re.search(r"(\d+)\.(\d+)", line).group()
            host['scan_start'] = re.search(r"\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}", line).group()
            host["hosts"] = {}
        # Scan finish time
        elif len(re.findall(r'(Nmap done)', line)):
            host['scan_finish'] = re.search(r"\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}", line).group()
        # Finding hosts and their status, creates new dict for each host
        elif  len(re.findall(r'(Host:).*(Status)', line)):
            host_line = re.search(re_host, line).group(2)
            host["hosts"][host_line] = {}
            host["hosts"][host_line]["host"] = host_line
            host["hosts"][host_line]["status"] = re.search(r'(Status: )(\w+)', line).group(2)
        # Extracts open ports for each host
        elif  len(re.findall(r'(Host:).*(Ports)', line)):
            host_line = re.search(re_host, line).group(2)
            host["hosts"][host_line]["ports"] = {}
            data = line.split("\t")
            data = data[1].split("Ports: ")
            data = data[1].split(", ")
            for port in data:
                port_data = port.split('/')
                host["hosts"][host_line]["ports"][port_data[0]] = {}
                host["hosts"][host_line]["ports"][port_data[0]]["port"] = port_data[0]
                host["hosts"][host_line]["ports"][port_data[0]]["state"] = port_data[1]
                host["hosts"][host_line]["ports"][port_data[0]]["protocol"] = port_data[2]
                host["hosts"][host_line]["ports"][port_data[0]]["idk1"] = port_data[3]
                host["hosts"][host_line]["ports"][port_data[0]]["service"] = port_data[4]
                host["hosts"][host_line]["ports"][port_data[0]]["idk2"] = port_data[5]
                host["hosts"][host_line]["ports"][port_data[0]]["banner"] = port_data[6]
                host["hosts"][host_line]["ports"][port_data[0]]["idk3"] = port_data[7]


    rfile.close()
    print_output(host)
    return 0

def print_output(host):
    format_string = "{0:20} {1}"
    init(autoreset=True)
    print(format_string.format('NMAP Version:', 'v' + host['nmap_version']))
    print(format_string.format("Scan Start:",host['scan_start']))
    print(format_string.format("Scan End:", host['scan_finish']))
    for h in host['hosts'].values():
        print(format_string.format("Host:", Fore.MAGENTA + h['host']))
        status_colour = Fore.RED
        if h['status'] == "Up":
            status_colour = Fore.GREEN
        print(format_string.format("Status:", status_colour + h['status']))

        for p in h['ports'].values():
            print("{} {}".format("\tPort:", Fore.YELLOW + p['port']))
            print(format_string.format("\t\tState:", p['state']))
            print(format_string.format("\t\tProtocol:", p['protocol']))
            print(format_string.format("\t\tService:", p['service']))
            print(format_string.format("\t\tBanner:", p['banner']))


    deinit()

if __name__ == '__main__':

    sys.exit(main(sys.argv[1:]))