# Variables
port = 21
banner = "FreeFloat FTP Server"
print("Checking for " + banner + " on port " + str(port))

# Strings
print(banner.upper())
print(banner.lower())
print(banner.replace('FreeFloat','Ability'))
print(banner.find('FTP'))

# Lists
portlist = []
portlist.append(21)
portlist.append(80)
portlist.append(443)
portlist.append(25)
print(portlist)
pos = portlist.index(80)
print("There are " + str(pos) + " ports to scan before 80.")
portlist.remove(443)
print(portlist)
cnt = len(portlist)
print("Scanning " + str(cnt) + " Total Ports.")

# Dictionaries
services = {'ftp':21,'ssh':22,'smtp':25,'http':80}
services.keys()
services.items()
services.has_key('ftp')
services['ftp']
print("Found vuln with FTP on port " + str(services['ftp']))

# Networking
import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.95.148",21))
ans = s.recv(1024)
print(ans)

# Selection
import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.95.148",21))
ans = s.recv(1024)
if ("FreeFloat Ftp Server (Version 1.00)" in ans):
    print("FreeFloat FTP Server is vulnerable.")
elif ("3Com 3CDaemon FTP Server (Version 2.0)" in ans):
    print("Vulnerable and so on")
else:
    print("Not vulnerable")

# Exception Handling
try:
    print("1337/0 = " + str(1337/0))
except:
    print("Error")
# This gives little information

try:
    print("1337/0 = " + str(1337/0))
except Exception as e:
    print("Error = " + str(e))
# Gives more information about type of Error

# Functions
import socket
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return

def main():
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    port = 21
    banner1 = retBanner(ip1, port)
    if banner1:
        print("[+] " + ip1 + ": " + banner1)
    banner2 = retBanner(ip2, port)
    if banner2:
        print("[+] " + ip2 + ": " + banner2)
if __name__ == '__main__':
    main()
##################################################

import socket
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print '[+] FreeFloat FTP Server is vulnerable.'
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print '[+] 3CDaemon FTP Server is vulnerable.'
    elif 'Ability Server 2.34' in banner:
        print '[+] Ability FTP Server is vulnerable.'
    elif 'Sami FTP Server 2.0.2' in banner:
        print '[+] Sami FTP Server is vulnerable.'
    else:
        print '[-] FTP Server is not vulnerable.'
        return
def main():
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    ip3 = '192.168.95.150'
    port = 21
    banner1 = retBanner(ip1, port)
    if banner1:
        print '[+] ' + ip1 + ': ' + banner1.strip('\n’)
        checkVulns(banner1)
    banner2 = retBanner(ip2, port)
    if banner2:
        print '[+] ' + ip2 + ': ' + banner2.strip('\n')
        checkVulns(banner2)
    banner3 = retBanner(ip3, port)
    if banner3:
        print '[+] ' + ip3 + ': ' + banner3.strip('\n')
        checkVulns(banner3)
if __name__ == '__main__':
    main()

# Iteration
for x in range(1,255):
    print("192.168.95."+str(x))

portlist = [21,22,25,80,110]
for port in portlist:
    print(port)

for x in range(1,255):
    for port in portlist:
        print("Checking 192.168.95."\
              +str(x)+": " +str(port))


# File I/O
def checkVulns(banner):
    f = open("vuln_banners.txt",'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print("[+] Server is vulnerable: " + banner.strip('\n'))

# Sys Module
import sys
if len(sys.argv)==2:
    filename = sys.argv[1]
    print("[+] Reading Vulnerabilities From: " + filename)

# OS Module
import sys
import os
if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("[-] " + filename + " does not exist.")
        exit(0)
    if not os.access(filename, os.R_OK):
        print("[-] " + filename + " access denied.")
        exit(0)
    print("[+] Reading Vulnerabilities From: " + filename)
