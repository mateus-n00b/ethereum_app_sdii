#!/usr/bin/env python2.7
import registered_functions as functions
import beacon_protocol
    
def run():
    # Starting beacons
    beacon_protocol.run()
    functions.run()

if __name__ == '__main__':
    run()
