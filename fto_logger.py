import time 
import datetime 
import sys


log = ''

def start_obj(log,ses_num):
    start_t = datetime.datetime.now()
    print(f'[+] OBSERVATION HAS STARTED... AT :{start_t}')
    log += f'[+] OBSERVATION HAS STARTED... AT :{start_t} \n'
    for i in range(1,ses_num):
        print(f"[+] SESSION {i} HAS STARTED")
        log += f"[+] SESSION {i} HAS STARTED \n"


def get_help():
    print('________ BELOW COMMANDS ARE ONLY ALLOWED ________')
    print('START or start or s or S ----- to start the observation timing')
    print('"END" or e or e or E --- to exit the process')
    
def take_cmd():
    while True:
        cmd = str(input("FTO_LOGGER >> ::"))
        if cmd == "START" or cmd == 'start' or cmd == 's' or cmd =='S':
            start_obj()
        elif cmd == "END" or cmd == 'end' or cmd == 'e' or cmd == 'E':
            sys.exit()
        elif cmd == "Help" or cmd == 'h':
            get_help()
        else:
            get_help()
    
