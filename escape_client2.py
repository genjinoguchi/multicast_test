import thread, threading
import time
import socket
import struct
import sys
import Queue

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

def if_statements_by_dennis():
    keep_dennis_running = True
    while (keep_dennis_running):
        print("if statements")
        time.sleep(0.5)
        print("by dennis li")
        time.sleep(0.5)
        print(keep_dennis_running)

        if not q.empty():
            keep_dennis_running = q.get_nowait()

while True:
    data, new_address = sock.recvfrom(10240)
    print >> sys.stderr, 'received %s (%s bytes) from %s' % (data, len(data), address)

    print >> sys.stderr, 'sending acknowledgement to address', address
    sock.sendto("ack", address)
