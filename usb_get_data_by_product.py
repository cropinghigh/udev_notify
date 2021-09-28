#!/usr/bin/env python
import sys
if(len(sys.argv) < 2):
    print("ERROR: not enough arguments")
    exit(1)
product = sys.argv[1]
pids = product.split("/")
pvid = pids[0].zfill(4)
ppid = pids[1].zfill(4)


f = open("/usr/share/hwdata/usb.ids", "r", encoding="utf8", errors='ignore');
devices = {}
curvendor = ""


for line in f:
    if(line.startswith("#") or len(line) <  7 or line[:1].isalpha()):
        continue
    line = line.replace("\n", "")
    tabs = line.count("\t")
    if(tabs == 0):
        sp = line.split("  ")
        vid = sp[0]
        vname = sp[1]
        devices[vid] = { "vname": vname }
        curvendor = vid
    elif(tabs == 1):
        sp = line.replace("\t", "").split("  ")
        did = sp[0]
        dname = sp[1]
        devices[curvendor][did] = dname

vendorname = devices[pvid]["vname"]
productname = devices[pvid][ppid]
print("'" + vendorname + " " + productname + "'" + "\nVendor id: " + pvid + "     Device id: " + ppid)
