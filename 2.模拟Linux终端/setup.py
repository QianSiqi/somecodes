import os
import socket
import sys
host = socket.gethostname()
link = '/'
while True:
    cd = ''
    enter = input(f'Administartor@{host} {link}:')
    if enter == 'quit()':
        sys.exit()
    elif 'cd ' in enter:
        cd = enter.split(' ')
        link += cd[1] + '/'
        os.chdir(cd[1])
        get = os.getcwd()
        os.system(f'cd {get}')
        os.system(enter)
    os.system('cd usr/bin')
    os.system(enter)
