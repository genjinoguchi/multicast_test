import thread
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

q = Queue.Queue()

def if_statements_by_dennis(address, port):
    keep_dennis_running = True
    while (keep_dennis_running):
        print("if statements")
        time.sleep(1)
        print("by dennis li")
        time.sleep(1)
        print("Address ", address)
        print("port ", port)
        time.sleep(1)

        if not q.empty():
            keep_dennis_running = q.get_nowait()
    print("Thread exiting: " + str(thread.get_ident()))

address = None

while True:
    data, new_address = sock.recvfrom(10240)
    print >> sys.stderr, 'received %s (%s bytes) from %s' % (data, len(data), new_address)

    print >> sys.stderr, 'sending acknowledgement to address', new_address
    sock.sendto("ack", new_address)

    if data == "STOP":
        q.put_nowait(False)
        break

    if (address != new_address):
        if address:
            q.put_nowait(False)
        thread.start_new_thread(if_statements_by_dennis, new_address)

    address = new_address
