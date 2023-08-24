"""imports"""
import shutil
import re
import os

"""FUNCTION FOR BANNER"""
def banner():
    os.system('cls')
    a1 = "═" * 52
    print()
    print("╔" + a1 + "╗")
    print("                      DUBANK                        ")
    print("╚" + a1 + "╝")

"""CLASS FOR VALIDATION"""
class Validation:

    # FUNCTION VALIDATION FOR ACCOUNT
    def filter():
        fh_log = open("PYTHON/user.txt", "r")
        s = fh_log.read()
        L = s.split("~")

        listUs = [] # list of user info
        removedash = [] # list of user info w/o other characters

        #transfer the data of txt file into a list
        for line in L:
            listUs.append(line)

        #removing other characters in the data
        for us_info in listUs:
            us_list = us_info.replace("\n","")
            removedash.append(us_list)

        user_list = removedash

        return user_list

    # FUNCTION VALIDATION FOR MOBILE NUMBER
    def valid_num(mob):
        return re.match(r'\b09?\d{9}$',mob)

    # FUNCTION VALIDATION FOR EMAIL
    def valid_email(ema):
        return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$', ema)

"""MAIN CLASS FOR USER"""
class User:

    def __init__(self,  accno, usname, upass, pin, bal, lname, fname, mob, ema, bday, usType, userReg):

        self.accno = accno
        self.usname = usname
        self.upass = upass
        self.pin = pin
        self.bal = bal
        self.lname = lname
        self.fname = fname
        self.mob = mob
        self.ema = ema
        self.bday = bday
        self.usType = usType
        self.userReg = userReg

    #FUNCTION FOR REGISTRATION
    def register(self):
        reg_w = open("PYTHON/user.txt", "a") 
        reg_w.write(self.accno+"~"+self.usname+"~"+self.upass+"~"+self.pin+"~"+self.bal+"~"+self.lname+"~"+self.fname+"~"+self.mob+"~"+self.ema+"~"+self.bday+"~"+self.usType+"~"+self.userReg+"~"+"\n")
        reg_w.close()
        shutil.copyfile('PYTHON/user.txt','PYTHON/user1.txt')
        shutil.copyfile('PYTHON/user1.txt','PYTHON/user2.txt')
        print("\n                Registration Success    ")
        print("          Thank you! for choosing DUBANK Online\n")

        
        

"""PROFILE CLASS"""
class Profile(User):


    def __init__(self,  accno, usname, upass, pin, bal, lname, fname, mob, ema, bday, usType, userReg):
        super().__init__(  accno, usname, upass, pin, bal, lname, fname, mob, ema, bday, usType, userReg)

        

    # FUNCTION FOR USER INFO
    def profile_user(self):

        us_log = open("PYTHON/user1.txt", "r")
        s_log=' '
        while(s_log):
            s_log = us_log.readline()
            L_log = s_log.split("~")

            if len(s_log)>0:
                if L_log[1] == self.usname and L_log[2] == self.upass:
                    accno = L_log[0]
                    usname = L_log[1]
                    pin = L_log[3]
                    bal = L_log[4]
                    lname = L_log[5]
                    fname = L_log[6]
                    mob = L_log[7]
                    ema = L_log[8]
                    bday = L_log[9]


                    return accno, usname, pin, fname, lname, bal, mob, ema, bday
    
    # FUNCTION FOR CHECK USER INFO
    def check_user(self):

        us_log = open("PYTHON/user1.txt", "r")
        s_log=' '
        while(s_log):
            s_log = us_log.readline()
            L_log = s_log.split("~")

            if len(s_log)>0:
                if L_log[0] == self.accno:
                    accno = L_log[0]
                    pin = L_log[3]
                    bal = L_log[4]
                    lname = L_log[5]
                    fname = L_log[6]

                    return accno, pin, fname, lname, bal



"""CLASS FOR DEPOSIT / CASH IN"""
class Deposit(User):

    def __init__(self, accno, usname, upass, pin, bal, lname, fname, mob, ema, bday, usType, userReg):
        super().__init__(accno, usname, upass, pin, bal, lname, fname, mob, ema, bday, usType, userReg)

        self.accno = accno
        self.bal = bal

    # FUNCTION FOR CASH IN
    def deposit(self):

        fh_s = open("PYTHON/user2.txt","r")
        fh_x = open("PYTHON/temp.txt","w")
        xs = ' '
        while(xs):
            xs=fh_s.readline()
            xpp=xs.split("~")
            if len(xs) > 0:
                if xpp[0]==self.accno:
                    balance = float(xpp[4]) + self.bal
                    fh_x.write(xpp[0]+"~"+xpp[1]+"~"+xpp[2]+"~"+xpp[3]+"~"+str(balance)+"~"+xpp[5]+"~"+xpp[6]+"~"+xpp[7]+"~"+xpp[8]+"~"+xpp[9]+"~"+xpp[10]+"~"+xpp[11]+"~"+"\n")
                else:
                    fh_x.write(xs) 

        fh_x.close()
        fh_s.close()
        os.remove("PYTHON/user2.txt")
        os.rename("PYTHON/temp.txt","PYTHON/user2.txt")
        shutil.copyfile('PYTHON/user2.txt','PYTHON/user.txt')
        shutil.copyfile('PYTHON/user.txt','PYTHON/user1.txt')

"""CLASS FOR WITHDRAW / CASH OUT"""
class With(User): 

    def __init__(self, accno, usname, upass, pin, bal, lname, fname, mob, ema, bday, usType, userReg):
        super().__init__(accno, usname, upass, pin, bal, lname, fname, mob, ema, bday, usType, userReg)

        self.accno = accno
        self.bal = bal

    # FUNCTION FOR CASH OUT / SEND CASH
    def withdraw(self):
        fh_with = open("PYTHON/user.txt","r")
        fh_draw = open("PYTHON/temp.txt","w")
        wd = ' '
        while(wd):
            wd=fh_with.readline()
            Lxpp=wd.split("~")
            if len(wd) > 0:
                if Lxpp[0]==self.accno:
                    balance = float(Lxpp[4]) - self.bal
                    fh_draw.write(Lxpp[0]+"~"+Lxpp[1]+"~"+Lxpp[2]+"~"+Lxpp[3]+"~"+str(balance)+"~"+Lxpp[5]+"~"+Lxpp[6]+"~"+Lxpp[7]+"~"+Lxpp[8]+"~"+Lxpp[9]+"~"+Lxpp[10]+"~"+Lxpp[11]+"~"+"\n")
                else:
                    fh_draw.write(wd)    

        fh_draw.close()
        fh_with.close()
        os.remove("PYTHON/user.txt")
        os.rename("PYTHON/temp.txt","PYTHON/user.txt")
        shutil.copyfile('PYTHON/user.txt','PYTHON/user1.txt')
        shutil.copyfile('PYTHON/user1.txt','PYTHON/user2.txt')

"""CLASS FOR CHANGINE PIN"""
class Change(User):

    def __init__(self, accno, usname, upass, pin, bal, lname, fname, mob, ema, bday, usType, userReg):
        super().__init__(accno, usname, upass, pin, bal, lname, fname, mob, ema, bday, usType, userReg)

        self.accno = accno
        self.pin = pin

    # FUNCTION FOR CHANGE PIN
    def change_pin(self):
        fh_with = open("PYTHON/user.txt","r")
        fh_draw = open("PYTHON/temp.txt","w")
        wd = ' '
        while(wd):
            wd=fh_with.readline()
            Lxpp=wd.split("~")
            if len(wd) > 0:
                if Lxpp[0]==self.accno:
                    fh_draw.write(Lxpp[0]+"~"+Lxpp[1]+"~"+Lxpp[2]+"~"+self.pin+"~"+Lxpp[4]+"~"+Lxpp[5]+"~"+Lxpp[6]+"~"+Lxpp[7]+"~"+Lxpp[8]+"~"+Lxpp[9]+"~"+Lxpp[10]+"~"+Lxpp[11]+"~"+"\n")
                else:
                    fh_draw.write(wd)    

        fh_draw.close()
        fh_with.close()
        os.remove("PYTHON/user.txt")
        os.rename("PYTHON/temp.txt","PYTHON/user.txt")
        shutil.copyfile('PYTHON/user.txt','PYTHON/user1.txt')
        shutil.copyfile('PYTHON/user1.txt','PYTHON/user2.txt')


