#!/usr/bin/env python3
# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]

approved_vendors = ["cisco","juniper","big_ip"]

# loop across the list vendors
for x in vendors:
    print("The vendor is:" + x)  # each time through the loop print value of x
    if x not in approved_vendors:   # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.") # print when loop has finished
