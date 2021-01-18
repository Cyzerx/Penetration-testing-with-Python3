import PortScanner

targets_ip = input(' [+] * Enter target to scan for Vulnerable Open Ports: ')
port_number = int(input('[+] * Enter amount of Ports you want to scan (500 - First 500 ports): '))
vuln_file = input('[+] * Enter path to the file with Vulnerable software: ')
print('\n')

target = PortScanner.PortScan(targets_ip, port_number)
target.scan()

with open(vuln_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + str(target.open_ports[count]))
        count += 1
