import time 
import datetime 
import sys


log = ''

def start_obj(log,ses):
    start_t = datetime.datetime.now()
    print(f'[+] OBSERVATION HAS STARTED... AT :{start_t}')
    log += f'[+] OBSERVATION HAS STARTED... AT :{start_t}'
    print(f"[+] SESSION {ses} HAS STARTED")
    

def take_input():
    while True:
        input = str("FTO_LOGGER >> ::")
        if input == "START" or 'start':
            start_obj()
        if input == "END" or 'end':
            sys.exit()
    
