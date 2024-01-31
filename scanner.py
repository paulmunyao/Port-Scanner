import socket
import sys
from datetime import datetime

target = input("Enter host to scan: ")
host = socket.gethostbyname(target)

print("Target: " + target)
print("Host: " + host)

date = datetime.date(datetime.now())
t1 = datetime.now()
print("Start Time: {}".format(t1.strftime("%H:%M:%S")))

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.000001)
    result = sock.connect_ex((host, port))
    if result == 0:
        try:
            print(
                "Port No : {} Open Protocol Service Name: {}".format(
                    port, socket.getservbyport(port, "tcp")
                )
            )
        except socket.error:
            print("Port No : {} OPen Protocol Service Name: {}".format(port, "Unknown"))

t2 = datetime.now()
print("End Time: {}".format(t2.strftime("%H:%M:%S")))

total_time = t2 - t1
print("Total time: {}".format(total_time))