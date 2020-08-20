import subprocess
import optparse
import re

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Used to select interface")
    parser.add_option("-m","--mac", dest="new_mac", help="Used to select mac")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("interface is not specified ! use -h (or) --help To get more information")
    elif not options.new_mac:
        parser.error("Mac Id is not specified ! use -h (or) --help To get more information")
    else:
        return options

def change_mac(interface, new_mac):
    print("Change Mac Address" + interface + " To "+ new_mac)
    subprocess.call(["ifconfig", interface,"down"])
    subprocess.call(["ifconfig", interface,"hw","ether", new_mac])
    subprocess.call(["ifconfig", interface,"up"])


def get_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    filter_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if filter_result:
        return filter_result.group(0)
    else:
        print("MAC Address Not Found")

options = get_options()

mac_address_filter_results = get_mac_address(options.interface)
print("Current MAC =" + str(mac_address_filter_results))

change_mac(options.interface, options.new_mac)

mac_address_filter_results = get_mac_address(options.interface)
if mac_address_filter_results == options.new_mac:
    print("Mac Address Changed To" + mac_address_filter_results)
else:
    print("Mac Address Is Not Changed")
