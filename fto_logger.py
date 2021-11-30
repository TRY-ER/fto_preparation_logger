import time 
import datetime 
import sys




def get_obj(log_own,ses_num):
    if ses_num == 1:
        print('[+] THIS IS OBSERVATION 1')
        log_own = log_own + "[+] THIS IS OBSERVATION 1 \n"
        start_t = datetime.datetime.now()
        print(f'    [+] OBSERVATION HAS STARTED... AT :{str(start_t)}')
        log_own = log_own + f"   [+] OBSERVATION HAS STARTED... AT :{str(start_t)} \n"
        for i in range(1,5):
            print(f"    [+] SESSION {str(i)} HAS STARTED")
            log_own = log_own + f"   [+] SESSION {str(i)} HAS STARTED \n"
            log_own = log_own + str(act_num_ses(i=i))  
        print(f'    [+] OBSERVATION HAS ENDED... AT :{datetime.datetime.now()}')
        log_own = log_own + f"    [+] OBSERVATION HAS ENDED... AT :{datetime.datetime.now()}\n"
        print('[+] THIS IS OBSERVATION 1')
        log_own = log_own + "[+] THIS IS OBSERVATION 1\n"
        return log_own
        
    else:
        ses = get_ses_num()
        print(f'[+] THIS IS OBSERVATION {str(ses)}')
        log_own = log_own + f'[+] THIS IS OBSERVATION {str(ses)}'
        start_t = datetime.datetime.now()
        print(f'    [+] OBSERVATION HAS STARTED... AT :{str(start_t)}')
        log_own = log_own + f'   [+] OBSERVATION HAS STARTED... AT :{str(start_t)} \n'
        for i in range(1,5):
            print(f"    [+] CLEANING SESSION {str(i)} HAS STARTED")
            log_own = log_own + f"   [+] CLEANING SESSION {str(i)} HAS STARTED \n"
            log_own = log_own + str(act_num_ses(i=i))
        print(f'    [+] OBSERVATION HAS ENDED... AT :{datetime.datetime.now()}')
        log_own = log_own + f'    [+] OBSERVATION HAS ENDED... AT :{datetime.datetime.now()}'
        print(f'[+] THIS IS OBSERVATION {str(ses)}')
        log_own = log_own + f'[+] THIS IS OBSERVATION :{str(ses)}'
        return log_own

def obj_iter():
    with open ('log.txt','r') as file:
        last_line = file.readlines()
        file.close()
    if len(last_line) != 0:
        return last_line[-1]
    else:
        return -1
def get_help():
    print('________ BELOW COMMANDS ARE ONLY ALLOWED ________')
    print('START or start or s or S ----- to start the observation timing')
    print('"END" or e or e or E --- to exit the process')
    
def take_cmd(log_own,ses_num):
    while True:
        cmd = str(input("FTO_LOGGER >> ::"))
        if cmd == "START" or cmd == 'start' or cmd == 's' or cmd =='S':
            main_log = get_obj(log_own,ses_num)
            return main_log
        elif cmd == "END" or cmd == 'end' or cmd == 'e' or cmd == 'E':
            sys.exit()
        elif cmd == "Help" or cmd == 'h':
            get_help()
        else:
            get_help()
    
    
def act_num_ses(i,log_own=""):
    if i == 1:
        print(f'[+] THE CLEANING WITH WATER AND SOAP HAS STARTED AT :: {datetime.datetime.now()}')
        log_own = log_own + f'   [+] THE CLEANING WITH WATER AND SOAP HAS STARTED AT :: {datetime.datetime.now()} \n'
        time.sleep(1500)
        print("[!!] FIVE MINUTE REMAINING TO CHANGE WATER TEMP .... ")
        time.sleep(180)
        print("[!!] TWO MINUTE REMAINING TO CHANGE WATER TEMP ....")
        cm  = str(input('[!!!] TIME TO CHANGE THE WATER TEMP:: did you change ?? [y/n]::'))
        while True:
            if cm == 'y' or 'Y':
                while True:
                    time.sleep(600)
                    print("[!!] FIVE MINUTE TO END THE SESSION .....")
                    time.sleep(300)
                    cm_ = str(input('[!!!] TIME TO END THE SESSION 1 :: did you change ?? [y/n]::'))
                    if cm_ == 'y' or 'Y':
                        print('[+] SESSION 1 ENDED SUCCESS FULLY')
                        log_own = log_own + f'   [+] THE CLEANING WITH WATER AND SOAP HAS ENDED AT :: {datetime.datetime.now()}\n'
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
                log_own = log_own + '[--] THE SESSION 1 EXPIRED WRT. TIME\n'
                cm_2 = str(input("[==] Do you want to do it any way ?? [y/n] "))
                if cm_2== "y" or cm_2 == "Y":
                    pass
                else:
                    print('[--] BREAKING THE ITERATION ...')
                    break
            else:
                print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
        return log_own
    elif i == 2:
        print(f'[+] THE CLEANING WITH DISTILLED WATER HAS STARTED AT :: {datetime.datetime.now()}')
        log_own = log_own + f'   [+] THE CLEANING WITH DISTILLED WATER HAS STARTED AT :: {datetime.datetime.now()} \n'
        time.sleep(1500)
        print("[!!] FIVE MINUTE REMAINING TO CHANGE WATER TEMP .... ")
        time.sleep(180)
        print("[!!] TWO MINUTE REMAINING TO CHANGE WATER TEMP ....")
        cm  = str(input('[!!!] TIME TO CHANGE THE WATER TEMP:: did you change ?? [y/n]::'))
        while True:
            if cm == 'y' or 'Y':
                while True:
                    time.sleep(600)
                    print("[!!] FIVE MINUTE TO END THE SESSION .....")
                    time.sleep(300)
                    cm_ = str(input('[!!!] TIME TO END THE SESSION 2 :: did you change ?? [y/n]::'))
                    if cm_ == 'y' or 'Y':
                        print('[+] SESSION 2 ENDED SUCCESS FULLY')
                        log_own = log_own + f'   [+] THE CLEANING WITH DISTILLED WATER HAS ENDED AT :: {datetime.datetime.now()} \n'
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
                cm_2 = str(input("[==] Do you want to do it any way ?? [y/n] "))
                if cm_2== "y" or cm_2 == "Y":
                    pass
                else:
                    print('[--] BREAKING THE ITERATION ...')
                    break
            else:
                print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
        return log_own
    elif i == 3:
        print(f'[+] THE CLEANING WITH ISOPROPANOL HAS STARTED AT :: {datetime.datetime.now()}')
        log_own = log_own + f'   [+] THE CLEANING WITH ISOPROPANOL HAS STARTED AT :: {datetime.datetime.now()} \n'
        time.sleep(1500)
        print("[!!] FIVE MINUTE REMAINING TO CHANGE WATER TEMP .... ")
        time.sleep(180)
        print("[!!] TWO MINUTE REMAINING TO CHANGE WATER TEMP ....")
        cm  = str(input('[!!!] TIME TO CHANGE THE WATER TEMP:: did you change ?? [y/n]::'))
        while True:
            if cm == 'y' or 'Y':
                while True:
                    time.sleep(600)
                    print("[!!] FIVE MINUTE TO END THE SESSION .....")
                    time.sleep(300)
                    cm_ = str(input('[!!!] TIME TO END THE SESSION 3 :: did you change ?? [y/n]::'))
                    if cm_ == 'y' or 'Y':
                        print('[+] SESSION 3 ENDED SUCCESS FULLY')
                        log_own = log_own + f'   [+] THE CLEANING WITH ISOPROPANOL HAS ENDED AT :: {datetime.datetime.now()} \n'
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
                cm_2 = str(input("[==] Do you want to do it any way ?? [y/n] "))
                if cm_2== "y" or cm_2 == "Y":
                    pass
                else:
                    print('[--] BREAKING THE ITERATION ...')
                    break
            else:
                print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
        return log_own
    elif i == 4:
        print(f'[+] THE CLEANING WITH ACETON HAS STARTED AT :: {datetime.datetime.now()}')
        log_own = log_own + f'   [+] THE CLEANING WITH ACETON HAS STARTED AT :: {datetime.datetime.now()} \n'
        time.sleep(1500)
        time.sleep(1500)
        print("[!!] FIVE MINUTE REMAINING TO CHANGE WATER TEMP .... ")
        time.sleep(180)
        print("[!!] TWO MINUTE REMAINING TO CHANGE WATER TEMP ....")
        cm  = str(input('[!!!] TIME TO CHANGE THE WATER TEMP:: did you change ?? [y/n]::'))
        while True:
            if cm == 'y' or 'Y':
                while True:
                    time.sleep(600)
                    print("[!!] FIVE MINUTE TO END THE SESSION .....")
                    time.sleep(300)
                    cm_ = str(input('[!!!] TIME TO END THE SESSION 4 :: did you change ?? [y/n]::'))
                    if cm_ == 'y' or 'Y':
                        print('[+] SESSION 4 ENDED SUCCESS FULLY')
                        log_own = log_own + f'   [+] THE CLEANING WITH ACETON HAS ENDED AT :: {datetime.datetime.now()} \n'
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
                cm_2 = str(input("[==] Do you want to do it any way ?? [y/n] "))
                if cm_2== "y" or cm_2 == "Y":
                    pass
                else:
                    print('[--] BREAKING THE ITERATION ...')
                    break
            else:
                print("[--] ENTER A VALID REPLY WITH y or Y or n or N")
        return log_own
    else:
        print("[!!!] SESSION GREATER THAN 4 HAS NOT BEEN CONSIDERED YET ...")
    

def get_ses_num():
    last_line = obj_iter()
    if last_line == -1 :
        return 1
    else:
        ses_num = last_line.split(":")[1]
        return int(ses_num)
    
def write_log_own(log_own):
    try:
        with open("log.txt","a") as file:
            file.write(log_own)
            print("[++] log_ownS SAVED IN log_own FILE")
    except:
        print("[--] CANNOT SAVE log_ownS")

if __name__  == "__main__":
    log_on = ''
    ses = get_ses_num()
    print(ses)
    main_log = take_cmd(log_own=log_on,ses_num=ses)
    main_log += "\n"
    main_log += f"OBSERVATION:{ses+1}"
    write_log_own(main_log)
