#!/usr/bin/env python3
import os
import sys
import struct

def to_addr(install):
    addr = ''
    with open("deployments/%s.addr" % install, "rb") as f:
        for _ in range(32):
            addr += "%.2x" % int.from_bytes(f.read(1), byteorder='big')
        wc = struct.unpack('!I', f.read(4))[0]
    print(str(wc) + ":" + addr)
    return str(wc) + ":" + addr

def run_client(cmd):
    os.system("lite-client -c '%s'" % cmd)

if sys.argv[1] == "send":
    run_client("last")
    run_client("sendfile deployments/last-query.boc")

elif sys.argv[1] == "acc":
    addr = to_addr(sys.argv[2])
    run_client("last")
    run_client("getaccount %s" % addr)

elif sys.argv[1] == "seqno":
    addr = to_addr(sys.argv[2])
    run_client("last")
    run_client("runmethod %s seqno" % addr)

elif sys.argv[1] == "version":
    addr = to_addr(sys.argv[2])
    run_client("last")
    run_client("runmethod %s version" % addr)

elif sys.argv[1] == "dnsresolve":
    addr = to_addr(sys.argv[2])
    domain = sys.argv[3]
    cat_id = int(sys.argv[4])
    run_client("last")

    run_client("runmethod %s dnsresolve %d \"%s\"" % (addr, cat_id, domain))