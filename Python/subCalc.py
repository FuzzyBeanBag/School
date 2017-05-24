#!/usr/bin/python
#==================================================
#
# NSSB 246 - Scripting
# Taylor McGee
# 5-14-2017
#
#==================================================

import sys
# Get address string and cidr string from command line
(addrString,cidrString) = sys.argv[1].split('/')

# split address into octets and turn cidr into int
addr = addrString.split('.')
cidr = int(cidrString)
#initialize the netmask and calculate based on cidr mask
mask = [0,0,0,0]

for i in range(cidr):
	mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
#initialize net and binary and netmask with addr to get network
	net = []

for i in range(4):
	net.append(int(addr[i]) & mask[i])
#duplicate net into broad array, gather host bits, and generate broadcast
	broad = list(net)
	brange = 32 - cidr

for i in range(brange):
	broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))

# Print information, mapping integer lists to strings for easy printing
print "Address: " , addrString
print "Netmask: " , ".".join(map(str,mask))
print "Network: " , ".".join(map(str,net))
print "Broadcast " , ".".join(map(str,broad))

