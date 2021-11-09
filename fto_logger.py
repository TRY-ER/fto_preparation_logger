import time 
import datetime 
import sys
import os


log = ''

def get_obj(log,ses_num):
    if not obj_iter():
        print('[+] THIS IS OBSERVATION 1')
        log += '[+] THIS IS OBSERVATION 1 \n'
        start_t = datetime.datetime.now()
        print(f'    [+] OBSERVATION HAS STARTED... AT :{start_t}')
        log += f'   [+] OBSERVATION HAS STARTED... AT :{start_t} \n'
        for i in range(1,ses_num+1):
            print(f"    [+] SESSION {i} HAS STARTED")
            log += f"   [+] SESSION {i} HAS STARTED \n"
            log += act_num_ses(i=i,log=log)
        print(f'    [+] OBSERVATION HAS ENDED... AT :{datetime.datetime.now()}')
        log += f'    [+] OBSERVATION HAS ENDED... AT :{datetime.datetime.now()}'
        print('[+] THIS IS OBSERVATION 1')
        log += '[+] THIS IS OBSERVATION 1'
        
    else:
        print(f'[+] THIS IS OBSERVATION {obj_iter()+1}')
        log += f'[+] THIS IS OBSERVATION {obj_iter()+1}'
        start_t = datetime.datetime.now()
        print(f'    [+] OBSERVATION HAS STARTED... AT :{start_t}')
        log += f'   [+] OBSERVATION HAS STARTED... AT :{start_t} \n'
        for i in range(1,ses_num):
            print(f"    [+] SESSION {i} HAS STARTED")
            log += f"   [+] SESSION {i} HAS STARTED \n"
            log += act_num_ses(i=i,log=log)
        print(f'    [+] OBSERVATION HAS ENDED... AT :{datetime.datetime.now()}')
        log += f'    [+] OBSERVATION HAS ENDED... AT :{datetime.datetime.now()}'
        print(f'[+] THIS IS OBSERVATION {obj_iter()+1}')
        log += f'[+] THIS IS OBSERVATION {obj_iter()+1}'
def obj_iter():
    with open ('log.txt','r') as file:
        for last_line in file.readline():
            pass
    return last_line[-1]

def get_help():
    print('________ BELOW COMMANDS ARE ONLY ALLOWED ________')
    print('START or start or s or S ----- to start the observation timing')
    print('"END" or e or e or E --- to exit the process')
    
def take_cmd():
    while True:
        cmd = str(input("FTO_LOGGER >> ::"))
        if cmd == "START" or cmd == 'start' or cmd == 's' or cmd =='S':
            get_obj()
        elif cmd == "END" or cmd == 'end' or cmd == 'e' or cmd == 'E':
            sys.exit()
        elif cmd == "Help" or cmd == 'h':
            get_help()
        else:
            get_help()
    
def act_num_ses(i,log):
    if i == 1:
        print(f'[+] THE CLEANING WITH WATER AND SOAP HAS STARTED AT :: {datetime.datetime.now()}')
        log += f'   [+] THE CLEANING WITH WATER AND SOAP HAS STARTED AT :: {datetime.datetime.now()} \n'
        time.sleep(1500)
        cm  = str(input('[!!!] TIME TO CHANGE THE WATER TEMP:: did you change ?? [y/n]::'))
        while True:
            if cm == 'y' or 'Y':
                while True:
                    time.sleep(1200)
                    cm_ = str(input('[!!!] TIME TO END THE SESSION 1 :: did you change ?? [y/n]::'))
                    if cm_ == 'y' or 'Y':
                        print('[+] SESSION 1 ENDED SUCCESS FULLY')
                        log += f'   [+] THE CLEANING WITH WATER AND SOAP HAS ENDED AT :: {datetime.datetime.now()}'
                        break
                    elif cm_ == 'n' or 'N':
                        print('[--] THE SESSION 1 EXPIRED WRT. TIME')
                        break
                    else:
                        print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
                        pass
                break
            elif cm == 'n' or 'N':
                print('[--] THE SESSION 1 EXPIRED WRT. TIME')
                break
            else:
                print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
                pass
    elif i == 2:
        print(f'[+] THE CLEANING WITH DISTILLED WATER HAS STARTED AT :: {datetime.datetime.now()}')
        log += f'   [+] THE CLEANING WITH DISTILLED WATER HAS STARTED AT :: {datetime.datetime.now()} \n'
        time.sleep(1500)
        cm  = str(input('[!!!] TIME TO CHANGE THE WATER TEMP:: did you change ?? [y/n]::'))
        while True:
            if cm == 'y' or 'Y':
                while True:
                    time.sleep(1200)
                    cm_ = str(input('[!!!] TIME TO END THE SESSION 2 :: did you change ?? [y/n]::'))
                    if cm_ == 'y' or 'Y':
                        print('[+] SESSION 2 ENDED SUCCESS FULLY')
                        log += f'   [+] THE CLEANING WITH DISTILLED WATER HAS ENDED AT :: {datetime.datetime.now()} \n'
                        break
                    elif cm_ == 'n' or 'N':
                        print('[--] THE SESSION 2 EXPIRED WRT. TIME')
                        break
                    else:
                        print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
                        pass
                break
            elif cm == 'n' or 'N':
                print('[--] THE SESSION 2 EXPIRED WRT. TIME')
                break
            else:
                print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
                pass
    elif i == 3:
        print(f'[+] THE CLEANING WITH ISOPROPANOL HAS STARTED AT :: {datetime.datetime.now()}')
        log += f'   [+] THE CLEANING WITH ISOPROPANOL HAS STARTED AT :: {datetime.datetime.now()} \n'
        time.sleep(1500)
        cm  = str(input('[!!!] TIME TO CHANGE THE WATER TEMP:: did you change ?? [y/n]::'))
        while True:
            if cm == 'y' or 'Y':
                while True:
                    time.sleep(1200)
                    cm_ = str(input('[!!!] TIME TO END THE SESSION 3 :: did you change ?? [y/n]::'))
                    if cm_ == 'y' or 'Y':
                        print('[+] SESSION 3 ENDED SUCCESS FULLY')
                        log += f'   [+] THE CLEANING WITH ISOPROPANOL HAS ENDED AT :: {datetime.datetime.now()} \n'
                        break
                    elif cm_ == 'n' or 'N':
                        print('[--] THE SESSION 3 EXPIRED WRT. TIME')
                        break
                    else:
                        print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
                        pass
                break
            elif cm == 'n' or 'N':
                print('[--] THE SESSION 3 EXPIRED WRT. TIME')
                break
            else:
                print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
                pass
    elif i == 4:
        print(f'[+] THE CLEANING WITH ACETON HAS STARTED AT :: {datetime.datetime.now()}')
        log += f'   [+] THE CLEANING WITH ACETON HAS STARTED AT :: {datetime.datetime.now()} \n'
        time.sleep(1500)
        cm  = str(input('[!!!] TIME TO CHANGE THE WATER TEMP:: did you change ?? [y/n]::'))
        while True:
            if cm == 'y' or 'Y':
                while True:
                    time.sleep(1200)
                    cm_ = str(input('[!!!] TIME TO END THE SESSION 4 :: did you change ?? [y/n]::'))
                    if cm_ == 'y' or 'Y':
                        print('[+] SESSION 4 ENDED SUCCESS FULLY')
                        log += f'   [+] THE CLEANING WITH ACETON HAS ENDED AT :: {datetime.datetime.now()} \n'
                        break
                    elif cm_ == 'n' or 'N':
                        print('[--] THE SESSION 4 EXPIRED WRT. TIME')
                        break
                    else:
                        print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
                        pass
                break
            elif cm == 'n' or 'N':
                print('[--] THE SESSION 4 EXPIRED WRT. TIME')
                break
            else:
                print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
                pass
    else:
        print("[!!!] SESSION GREATER THAN 4 HAS NOT BEEN CONSIDERED YET ...")
    return log

if __name__  == "__main__":
    pass