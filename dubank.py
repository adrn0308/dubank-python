
"""imports"""
import os
import getpass
import oop
from random import randint
import datetime


"""variables for the account"""
us_acc = ""
us_id = ""
us_pas = ""
us_pin = ""
us_bal = ""
us_las = ""
us_pers = ""
us_mob = ""
us_ema = ""
us_day = ""
us_type = ""
us_reg = ""
send_amo = 0.0

u_reg = datetime.datetime.now() 
d_sign = " ---------------------------------------------------- "
cycle = True
msg = " "

"""HOMEPAGE"""
while cycle:
    oop.banner()
    print(d_sign)
    print(msg)
    print("                    DUBANK Online")
    print("       Expertise you need. Service you deserver!\n")
    print("   [1]Login | [2]Register | [3]Cash IN | [4]Cash OUT")
    print(d_sign)
    resp = input(" Select: ")

    #LOGIN PAGE
    if resp == '1':
        oop.banner()
        print(d_sign)
        us = input("              User ID  : ")
        ps = getpass.getpass("              Password : ")
        try:
            filter_acc = oop.Validation
            filter_acc.filter()
            if us in filter_acc.filter() and ps in filter_acc.filter():

                pro = oop.Profile(us_acc, us, ps, us_pin, us_bal, us_las, us_pers, us_mob, us_ema, us_day, us_type, us_reg)
                pro.profile_user()

                user_info = {
                    'acc_number': pro.profile_user()[0],
                    'user_name': pro.profile_user()[1],
                    'pin_number': pro.profile_user()[2],
                    'persname': pro.profile_user()[3],
                    'lasname': pro.profile_user()[4],
                    'balance': pro.profile_user()[5],
                    'mobile': pro.profile_user()[6],
                    'email': pro.profile_user()[7],
                    'berday': pro.profile_user()[8],
                }



                s1 = []
                s2 = []
                s3 = []
                s1.append(user_info['persname'])
                s2.append(user_info['lasname'])
                s3.append(user_info['acc_number'])
                x = str(s1)
                z = str(s2)
                w = str(s3)
                intial = x[2]+z[2]
                in_acc = " **"+w[10:14]
                
                # USER DASHBOARD
                ikot = True
                while ikot:
                    oop.banner()
                    print(d_sign)
                    result = float(user_info['balance']) - send_amo
                    print(" [",intial,"] Dashboard         ",u_reg)
                    print(d_sign)
                    print("",user_info['persname']+" "+user_info['lasname'])
                    print(" Personal Savings")
                    print(in_acc)
                    print("                                       Avail. Balance")
                    print("                                         PHP",result)
                    print(d_sign)
                    print("        [1] Send Cash    |   [2] View Account\n        [3] Change PIN   |   [4] Logout")
                    print(d_sign)
                    resp1 = input(" Select: ")

                    # SEND CASH FROM OTHER ACCOUNTS
                    if resp1 == '1':
                        oop.banner()
                        print(d_sign)
                        print(" [ Send Cash ]            ", u_reg)
                        print(d_sign)
                        print(" Sender:")
                        print(" Account Name  : ",user_info['persname']+" "+user_info['lasname'])
                        print(" Account Number: ",user_info['acc_number'])
                        print(d_sign)
                        print(" Reciever:")
                        send_name = input(" Account Name : ")
                        send_acc = input(" Account No.  : ")
                        print(d_sign)
                        send_amo = float(input(" Enter Amount   : "))
                        pin1 = getpass.getpass(" Enter your PIN : ")

                        if pin1 == user_info['pin_number']:
                            if send_amo > float(user_info['balance']):
                                print(d_sign)
                                send_amo = 0
                                print("                [ Insuficient Balance ]")
                                print("           You need to Cash IN immediately")
                                input("           Press enter to go Dashboard......")
                                ikot = True
                            else:    
                                print(d_sign)                  
                                print("             [1]Proceed  |  [2]Cancel")
                                print(d_sign)
                                sel = input(" Select: ")

                                if sel == '1':
                                    snd = oop.Deposit(send_acc, us_id, us_pas, us_pin, send_amo, us_las, us_pers, us_mob, us_ema, us_day, us_type, us_reg)
                                    snd.deposit()
                                    snd1 = oop.With(user_info['acc_number'], us, ps, us_pin, send_amo, us_las, us_pers, us_mob, us_ema, us_day, us_type, us_reg)
                                    snd1.withdraw()
                                    oop.banner()
                                    print(d_sign)
                                    print("\n                Transaction Success    ")
                                    print("          Thank you! for using DUBANK Online\n")
                                    print(d_sign)
                                    print(" Sender:")
                                    print(" Account Name : ",user_info['persname']+" "+user_info['lasname'])  
                                    print(" Account No.  : ",user_info['acc_number']) 
                                    print(d_sign)
                                    print(" Reciever:")
                                    print(" Account Name : ", send_name)  
                                    print(" Account No.  : ", send_acc) 
                                    print(d_sign)
                                    print(" Amount       : PHP",send_amo) 
                                    print(d_sign)
                                    print(" Transaction type: Send Cash")
                                    print(" Date / Time : ", u_reg)
                                    print(d_sign)
                                    input("           Press enter to go Homepage......")
                                    ikot = True
                                        
                        else:
                            print(d_sign)
                            input("          [ The PIN entered is incorrect ]\n          Press enter go Dashboard......")
                            ikot = True
                    
                    # VIEW ACCOUNT DETAILS
                    elif resp1 == '2':
                        oop.banner()
                        print(d_sign)
                        print(" [",intial,"] Account Details  ", u_reg)
                        print(d_sign)
                        print(" Account Name  : ",user_info['persname']+" "+user_info['lasname'])
                        print(" Account Number: ",user_info['acc_number'])
                        print(" Birthdate     : ",user_info['berday'])
                        print(d_sign)
                        print(" Email Address  : ",user_info['email'])
                        print(" Mobile No.     : ",user_info['mobile'])
                        print(d_sign)
                        input("           Press enter to go Dashboard......")
                    
                    # CHANGING PIN NUMBER
                    elif resp1 == '3':

                        ikot1 = True
                        mesg = ""
                        while ikot1:
                            oop.banner()
                            print(d_sign)
                            print(" [",intial,"] Change PIN    ", u_reg)
                            print(d_sign)
                            print(mesg)
                            old_pin = getpass.getpass(" Old PIN No. : ")
                            if old_pin == user_info['pin_number']: 
                                print(d_sign)
                                new_pin = getpass.getpass(" Create New PIN No.  : ")
                                if len(new_pin)==6:
                                    new_pin1 = getpass.getpass(" Confirm PIN No.  : ")
                                    if new_pin == new_pin1:
                                        print(d_sign)
                                        print("             [1]Proceed  |  [2]Cancel")
                                        sel3 = input(" Select : ")
                                        if sel3 == '1':
                                            cha_pin = oop.Change(user_info['acc_number'], us, ps, new_pin, send_amo, us_las, us_pers, us_mob, us_ema, us_day, us_type, us_reg)
                                            cha_pin.change_pin()
                                            oop.banner()
                                            print(d_sign)
                                            print("\n                Change PIN Success    ")
                                            input("           Press enter to go Dashboard......")
                                            ikot1 = False
                                            ikot = True
                                        else:
                                            ikot1 = False    
                                            ikot = True                  
                                    else:
                                        mesg = "                                  PIN DID NOT MATCH"
                                        ikot1 = True
                                else:
                                    mesg = "                                PIN MUST BE 6 DIGITS"
                                    ikot1 = True     
                            else:
                                mesg = "                                     PIN IS INCORRECT"
                                ikot1 = True

                    elif resp1 == '4':
                        msg = ""
                        ikot = False
                        cycle = True
            else:
                msg = "            [ Invalid User ID / Password ]"
                cycle = True

        except Exception as e:
                if len(ps) == 6:
                    msg = "            [ Invalid User ID / Password ]"
           
    # REGISTRATION FOR NEW ACCOUNT
    elif resp == '2':
        oop.banner()
        print(d_sign)
        print(" Personal Savings         ", u_reg)
        print(d_sign)
        print(" [ Personal Information ] ")
        print(d_sign)
        l_name = input(" Lastname: ")
        f_name = input(" Firstname: ")
        b_day = input(" Date of Birth *\n (ex. DD/MM/YYYY)  : ")

        msg1 = ""
        cycle1 = True
        while cycle1:
            print(msg1)
            m_no = input(" Mobile no. *\n (ex. 09********) : ")
            x = oop.Validation
            print(d_sign)
            if x.valid_num(m_no):
                
                msg2 = "" 
                cycle2 = True
                while cycle2:
                    print(msg2)
                    e_ma = input(" Email Adress *  : ")
                    if x.valid_email(e_ma):
                        oop.banner()
                        print(d_sign)
                        print(" [ Login Credentials ]")
                        print(d_sign)
                        usname = input(" Username *   : ")
                    
                        msg3 = ""
                        cycle3 = True
                        while cycle3:
                            print(msg3)
                            upass = getpass.getpass(" Password *   : ")

                            if len(upass) >= 8:
                                upass2 = getpass.getpass(" Confirm Password *  : ")
                                if upass2 == upass:

                                    msg4 = ""
                                    cycle4 = True
                                    while cycle4:
                                        oop.banner()
                                        print(d_sign)
                                        print(" [ MPIN Info ]")
                                        print(d_sign)
                                        print(msg4)
                                        upin = getpass.getpass(" PIN No. (6 digits)   :  ")
                                        if len(upin) == 6:
                                            print(d_sign)
                                            print("             [1]Proceed  |  [2]Cancel")
                                            print(d_sign)
                                            resp1 = input(" Select: ")
                                            if resp1 == '1':
                                                n = 10
                                                range_start = 10**(n-1)
                                                range_end = (10**n)-1
                                                accountNumber = randint(range_start, range_end)
                                                x1 = 0
                                                y1 = str(x1) + str(x1)
                                                acc_no = (str(y1)+str(accountNumber)) 
                                                acc_bal = 0  
                                                us_type = 1    
                                                reg = oop.User(acc_no,usname,upass,upin,str(acc_bal),l_name,f_name,m_no,e_ma,b_day,str(us_type),str(u_reg))
                                                oop.banner()
                                                print(d_sign)
                                                reg.register()
                                                print(d_sign)
                                                input("        Press enter to Homepage.....")
                                                cycle4 = False
                                                cycle3 = False
                                                cycle2 = False
                                                cycle1 = False
                                                cycle = True
                                            else:
                                                cycle4 = False
                                                cycle3 = False
                                                cycle2 = False
                                                cycle1 = False
                                                cycle = True
                                        else:
                                            msg4 = "                            PIN NO. MUST BE 6 DIGITS"
                                            cycle4 = True

                                else:
                                    msg3 = "                               PASSWORD DID NOT MATCH"
                                    cycle3 = True

                            else:
                                msg3 = "                    PASSWORD MUST BE 8 DIGITS OR MORE"
                                cycle3 = True
                    else:
                        msg2 = "                                INVALID EMAIL ADDRESS"
                        cycle2 = True
                    
            else:
                msg1 = "                                   INVALID MOBILE NO."
                cycle1 = True
    
    # CASH IN PAGE
    elif resp == '3':
        oop.banner()
        print(d_sign)
        print(" [ Cash IN ]              ",u_reg)
        print(d_sign)
        account_name = input(" Enter Account Name : ")
        account_num = input(" Enter Account No. : ")
        print(d_sign)
        valid_account = oop.Validation
        valid_account.filter()

        if account_num in valid_account.filter():

            pro = oop.Profile(account_num, us_id, us_pas, us_pin, us_bal, us_las, us_pers, us_mob, us_ema, us_day, us_type, us_reg)
            pro.check_user()

            user_info = {
                'acc_number': pro.check_user()[0],
                'pin_number': pro.check_user()[1],
                'persname': pro.check_user()[2],
                'lasname': pro.check_user()[3],
                'balance': pro.check_user()[4],
            }


            amount = float(input(" Enter Amount: "))
            print(d_sign)
            account_pin = getpass.getpass(" Enter you PIN: ")
            

            if account_pin == user_info['pin_number']:
                print(d_sign)
                print("             [1]Proceed  |  [2]Cancel")
                sel2 = input(" Select : ")
                if sel2 == '1':
                    send = oop.Deposit(user_info['acc_number'], us_id, us_pas, us_pin, amount, us_las, us_pers, us_mob, us_ema, us_day, us_type, us_reg)
                    send.deposit()
                    oop.banner()
                    print(d_sign)
                    print("\n                Transaction Success    ")
                    print("          Thank you! for using DUBANK Online\n")
                    print(d_sign)
                    print(" Account Name : ",user_info['persname']+" "+user_info['lasname'])  
                    print(" Account No.  : ",user_info['acc_number']) 
                    print(d_sign)
                    print(" Amount           : PHP",amount) 
                    result = float(user_info['balance']) + amount
                    print(" Your new Balance : PHP", result)
                    print(d_sign)
                    print(" Transaction type: Cash IN")
                    print(" Date / Time : ", u_reg)
                    print(d_sign)
                    input("           Press enter to go Homepage......")
                else:
                    cycle = True

            else:
                print(d_sign)
                input("          [ The PIN entered is incorrect ]\n          Press enter go Homepage......")

        else:
            oop.banner()
            print("               Transaction Failed    ")
            input("          [ Account Details is incorrect ]\n          Press enter go Homepage......")

    # CASH OUT PAGE
    elif resp == '4':
        oop.banner()
        print(d_sign)
        print(" [ Cash OUT ]             ",u_reg)
        print(d_sign)
        account_name = input(" Enter Account Name : ")
        account_num = input(" Enter Account No. : ")
        print(d_sign)
        valid_account = oop.Validation
        valid_account.filter()

        if account_num in valid_account.filter():

            pro = oop.Profile(account_num, us_id, us_pas, us_pin, us_bal, us_las, us_pers, us_mob, us_ema, us_day, us_type, us_reg)
            pro.check_user()

            user_info = {
                'acc_number': pro.check_user()[0],
                'pin_number': pro.check_user()[1],
                'persname': pro.check_user()[2],
                'lasname': pro.check_user()[3],
                'balance': pro.check_user()[4],
            }


            amount = float(input(" Enter Amount: "))
            print(d_sign)
            account_pin = getpass.getpass(" Enter you PIN: ")
            

            if account_pin == user_info['pin_number']:
                print(d_sign)
                print("             [1]Proceed  |  [2]Cancel")
                sel2 = input(" Select : ")
                if sel2 == '1':
                    send = oop.With(user_info['acc_number'], us_id, us_pas, us_pin, amount, us_las, us_pers, us_mob, us_ema, us_day, us_type, us_reg)
                    send.withdraw()
                    oop.banner()
                    print(d_sign)
                    print("\n                Transaction Success    ")
                    print("          Thank you! for using DUBANK Online\n")
                    print(d_sign)
                    print(" Account Name : ",user_info['persname']+" "+user_info['lasname'])  
                    print(" Account No.  : ",user_info['acc_number']) 
                    print(d_sign)
                    print(" Amount           : PHP",amount) 
                    result = float(user_info['balance']) - amount
                    print(" Your new Balance : PHP", result)
                    print(d_sign)
                    print(" Transaction type: Cash OUT")
                    print(" Date / Time : ", u_reg)
                    print(d_sign)
                    input("           Press enter to go Homepage......")
                else:
                    cycle = True

            else:
                print(d_sign)
                input("          [ The PIN entered is incorrect ]\n          Press enter go Homepage......")

        else:
            oop.banner()
            print("               Transaction Failed    ")
            input("          [ Account Details is incorrect ]\n          Press enter go Homepage......")
    else:
        msg = "                [ Invalid Selection ]"
        cycle = True1