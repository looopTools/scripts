#!/usr/bin/env python3

# get-mac-address
# by: tools

from uuid import getnode as get_mac
import socket
# Returns a 48 bit integer
# representing the mac address of the system
def mac():
    return get_mac()

def ip():
    sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sck.connect(("8.8.8.8", 80))
    ip = sck.getsockname()[0]
    sck.close()
    return ip
