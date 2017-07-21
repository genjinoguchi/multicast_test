import socket
import struct
import sys

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
TIMEOUT = 2  # in seconds
message = "very important data, not very securely sent"


# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Set timeout
sock.settimeout(TIMEOUT)

# Set time-to-live
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, (MCAST_GRP, MCAST_PORT))

    while True:
        print >> sys.stderr, 'waiting to receive'
        try:
            data, server = sock.recvfrom(16)

        except socket.timeout:
            print >> sys.stderr, 'timed out, no more response'
            break
        else:
            print >> sys.stderr, 'received "%s" from %s' % (data, server)
finally:
    print >> sys.stderr, 'closing socket'
    sock.close()
