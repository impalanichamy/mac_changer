#!/usr/bin/env python
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", help="enter interface name to change mac address", dest="interface")
    parser.add_option("-m", "--mac", help="Enter the new mac address", dest="new_mac")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] specify the interface. for more info use --help")
    if not options.new_mac:
        parser.error("[-] specify the new mac address. for more info use --help")
    return options
    
    
def change_mac(interface, new_mac):
    print("[+] changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
