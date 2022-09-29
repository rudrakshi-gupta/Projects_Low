print("\n\t\t\t\t**********************************\n")
print("\n\t\t\t\t      DOODLEY POODLEY BANK\n")
print("\n\t\t\t\t**********************************")


class Info:

    def __init__(self,name,age,gender,phone_no,password,cash):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone_no=phone_no
        self.__password=password
        self.cash=cash

    def __str__(self):
        print("\n-------------------------------------------------------------------------------\n")
        print(f'\n\nClient name : {self.name}\nClient age : {self.age}\nClient gender : {self.gender}\nClinet Phone number : {self.phone_no}\nCash bonus for creating an account : 100 Rs\n')
        print("\n-------------------------------------------------------------------------------\n")

print("\n\t\t\t\t\t     WELCOME!!\n")
print("\n\nINSTRUCTIONS :-\n*The name you enter now will be final name,\n  it can't be modified later as your file will be addressed by your name.\n*Password length only allowed from 5 to 15.\n  Do memorise your password to login.\n")
print("\nHave an account??\n1---Login\nOr\n2---Create a new account\n")
choice=int(input("Enter your choice here : "))

def display(name):
    with open(f"{name}.txt","r") as f:
        display=f.read()
        print("\n-------------------------------------------------------------------------------\n")
        k=display.split("\n")
        print(f"Name : {name}")
        print(f"\nAge : {k[1]}")
        print(f"\nGender : {k[2]}")
        print(f"\nPhone number : {k[3]}")
        print("\n-------------------------------------------------------------------------------\n")

if(choice==2):
    name=input("Name : ")
    age=int(input("Age : "))
    gender=input("Gender(M/F) : ")
    phone_number=int(input("Phone Number : "))
    if(len(str(phone_number))!=10):
        print("\nPhone number has less or more than 10 digits.Enter again.\n")
        phone_number=int(input("Phone Number : "))
    password=input("Password : ")
    if(len(str(password))<5 or len(str(password))>15):
        print("\nPassword length only allowed from 5 to 15.Enter again.\n")
        password=input("Password : ")
    details=[name,age,gender,phone_number]
    secure_details=[name,password,100]
    with open(f"{name}_s.txt","w") as file:
        for i in range(len(secure_details)):
            file.write(str(secure_details[i])+"\n")
    with open(f"{name}.txt","w") as f:
        for i in range(len(details)):
            f.write(str(details[i])+"\n")
    client=Info(name,age,gender,phone_number,password,100)
    print("\n\t\t\t\tAccount has been created.\n\n")
    # print(client.__dict__)
    # print(client.__password)
    print(client)

if(choice==1):
    
    class Bank:

        def __init__(self,name):
            self.l=[]
            self.cash=0
            self.name=name

        #roo
        def login(self):
            try:
                b=input("Enter your Password : ")
                self.__password=b
                with open(f"{self.name}_s.txt","r") as f:
                    checking_info=f.read().split("\n")
                    # self.name=checking_info[0]
                    if (self.__password == checking_info[1]):
                        print("\n\t\t\t\tSuccessful Login.\n")
                        return 5

                    else:
                        print("\n\t\t\t\t\tWrong details.\n\t\t\t    Exit and try Again.\n")

            except FileNotFoundError:
                print("\n\n\t\t\t\tNAME is incorrect, enter a valid name_id.\n")
        #arman
        def check_bal(self):
            with open(f"{self.name}_s.txt","r") as f:
                self.l=f.read().split("\n")
                print(f'Cash Balance = {self.l[2]}')
                if(self.l[2]==0):
                    print("\nEmpty Bank account. You are broke.\n")
            
        #esha
        def deposit_am(self,amount):
            if(amount!=0):
                with open(f"{self.name}_s.txt","r") as f:
                    d=f.read()
                    self.l=d.split("\n")
                    self.cash=int(self.l[2])
                    self.cash+=amount
                with open(f"{self.name}_s.txt","w") as f:
                    f.write(d.replace(self.l[2],str(self.cash)))
            
                print(f"The amount = {amount} has been deposited in your bank account.")

            else:
                print("Enter a valid amount to be deposited.")
                
        #bhanu
        def withdraw_am(self,amount):
            with open(f"{self.name}_s.txt","r") as f:
                d=f.read()
                self.l=d.split("\n")
                self.cash=int(self.l[2])
                if(self.cash!=0 and amount<=self.cash):
                    self.cash-=amount
                    with open(f"{self.name}_s.txt","w") as f:
                        f.write(d.replace(self.l[2],str(self.cash)))
                    print(f"Withdrawal Successful. Amount = {amount} has been withdrawed")

                else:
                    print("\nYou are poor.\n")

            
        #roo
        def transfer_am(self,amount,sender):
            
            with open(f"{self.name}_s.txt","r") as f:
                d=f.read()
                self.l=d.split("\n")
                self.cash=int(self.l[2])
                if(self.cash!=0 and amount<=self.cash):
                    self.cash-=amount
            with open(f"{self.name}_s.txt","w") as f:
                f.write(d.replace(self.l[2],str(self.cash)))
            
            try:
                with open(f"{sender}_s.txt","r") as file:
                    s=file.read()
                    self.l=s.split("\n")
                    self.cash=int(self.l[2])
                    if(self.cash!=0):
                        self.cash+=amount
                with open(f"{sender}_s.txt","w") as file:
                    file.write(s.replace(self.l[2],str(self.cash)))

                print(f"Amount = {amount} has been transferred successfully to {sender}")
            
            except FileNotFoundError:
                print(f"\n{sender}'s bank account dosen't exist.\n")
                
            
        #roo and durgesh
        def edit_profile(self):

            print("\n1---Age\n2---Gender\n3---Phone number\n4---Password")
            i=int(input("\n\nEnter the field no. that you want to edit : "))

            if(i==1):
                age_f=input("\nEnter you correct age :")
                with open(f"{self.name}.txt","r") as f:
                    d=f.read()
                    self.l=d.split("\n")
                with open(f"{self.name}.txt","w") as file:
                    file.write(d.replace(self.l[1],str(age_f)))

            if(i==2):
                with open(f"{self.name}.txt","r") as f:
                    d=f.read()
                    self.l=d.split("\n")
                gender_f=input("\nEnter you gender :")
                with open(f"{self.name}.txt","w") as file:
                    file.write(d.replace(self.l[2],str(gender_f)))

            if(i==3):
                with open(f"{self.name}.txt","r") as f:
                    d=f.read()
                    self.l=d.split("\n")
                ph_f=input("\nEnter you phone number :")
                with open(f"{self.name}.txt","w") as file:
                    file.write(d.replace(self.l[3],str(ph_f)))

            if(i==4):
                password_new=input("\nEnter you new password :")
                with open(f"{self.name}_s.txt","r") as f:
                    s=f.read()
                    self.l=s.split("\n")
                with open(f"{self.name}_s.txt","w") as file:
                    file.write(s.replace(self.l[1],str(password_new)))
            
            
        #durgesh 
        @staticmethod
        def log_out():
            print("\n-------------------------------------------------------------------------------\n")
            print("\n\n\t\t\t\tThank you.\n\t\t\t\tVisit again.\n\n\t\t\t     You logged out......\n")
            print("\n-------------------------------------------------------------------------------\n")
            exit()

    #main
    print("\nEnter your Name and Password to login.\n")
    a=input("Enter you name : ")
    client=Bank(a)
    c=client.login()
    while(c==5):
        print("\n-------------------------------------------------------------------------------\n")
        print("\n\nMenu :-\n\t1---Check Balance\n\t2---Deposit Amount\n\t3---Withdraw amount\n\t4---Transfer Amount\n\t5---Edit Profile\n\t0---Log out\n")
        decision=int(input("\nSelect option : "))
        if(decision==1):
            print("\nThis is banks's option to check balance.......\n")
            client.check_bal()
        if(decision==2):
            print("\nThis is bank's depositing option......\n")
            am=int(input("Enter the amount to be deposited : "))
            client.deposit_am(am)
        if(decision==3):
            print("\nThis is bank's withdrawal option......\n")
            am=int(input("Enter the amount to be withdrawan : "))
            client.withdraw_am(am)
        if(decision==4):
            print("\nThis is bank's transfer option......\n")
            am=int(input("Enter the amount to be transfered : "))
            send=input("\nEnter the name of the person cash to be transfered(eg.Tony) : ")
            client.transfer_am(am,send)
        if(decision==5):
            display(a)
            client.edit_profile()
            display(a)
        if(decision==0):
            client.log_out()