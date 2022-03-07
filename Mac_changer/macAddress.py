import subprocess
import optparse
import re

# MAC Changer or Physical Address
# MAC Stands for (Media Access Controlle)

# Every Device has a uniq Mac-Address
# First three part of the Address identify the "Device"
# Last three part of the Address identify the "Manufacture of the Device"
# Mac-Address Spoofing


# subprocess enables us to run ystem commands
# optparse used to parse arguments in our program such as the Mac-Address and interface
# re used for the Regular Expression


def get_arguments():
    # Creating an object that can handles user inputs from the Command-Line
    parser = optparse.OptionParser()

    # Adding Options to the Object
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's Mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAc address")
    (options, arguments) = parser.parse_args()

    # Control Structure 
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parse.error("[-] Please specify a new MAC address, use --help for more info")

    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



