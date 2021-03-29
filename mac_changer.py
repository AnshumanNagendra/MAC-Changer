#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC to change its mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please enter an interface or use help")
    elif not options.new_mac:
        parser.error("Please enter new mac or use help")
    return options

def change_mac(interface, new_mac):
    print("Changing mac address " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    interface_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interface_result)
    if mac_address_search_result:
       return mac_address_search_result.group(0)
    else:
        print("Could not find mac address")

options= get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC" +current_mac)

change_mac(options.interface, options.new_mac)



current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("MAC Address was successfully changed to" +current_mac)
else:
    print("MAC Address did not change")