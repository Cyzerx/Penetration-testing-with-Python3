import socket
from IPy import IP

def scan(target):
    converted_ip = ip_check(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    for port in range(20, 85):
        port_scan(converted_ip, port)

def ip_check(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) #Some ports take longer to connect, the lower the timeout the lower the accuracy
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open port ' + str(port))
    except:
        pass

if __name__ == "__main__":
    targets = input('[+] Enter target/s to scan (split multiple targets with ,): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
