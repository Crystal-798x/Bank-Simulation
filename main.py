import sys
import pickle
import random
# Account = {Acccount_Number: Name, Amount, History, Status }
Account = { 22344322 : ["Abdul Salam", 30000,{0 : "Account Created"}],   
            21344312 :  ["Eshan", 30000,{0 : "Account Created"}],
            }
try:
    with open('data.pkl', 'rb') as file:
        Account = pickle.load( file) 
except FileNotFoundError:  
    print("Error Code 404")
except pickle.UnpicklingError, EOFError,SyntaxError:
    print("An Error Occured:")
    sys.exit()    
  
wel = "Welcome To Crystal Bank Limited \n "
print(wel)
def C_time():
    import time
    from time import strftime
    time = time.localtime()
    hourly_time = strftime("%a-%d-%b-%Y-%H:%M:%S", time)
    return hourly_time 
def deposit():
    try:
        amount = int(input("Enter the amount to deposit: "))
    except ValueError:
        print("Enter The Correct Amount")  
        return sngl_acc[1]
    if amount<=0:
        print("Enter the Right Figure")
        return sngl_acc[1]
    else:
        namount=sngl_acc[1] + amount
        sngl_acc[1] = namount
        count = sngl_acc[2]
        count_key = max(count)+1
        sngl_acc[2][count_key] = f"Deposited Amount {amount} With New Balance As {sngl_acc[1]} At {C_time()}"
    return namount
def withdraw():
        try:
            amount = int(input("Enter the amount to withdraw: "))
        except ValueError:
            print("Enter The Correct Amount")
            return sngl_acc[1]
        if amount<=0:
            print("Enter the Right Figure")
            return sngl_acc[1]
        elif amount>sngl_acc[1]:
            print("You fucking thiefffff")
            return sngl_acc[1]
        else:    
            namount=sngl_acc[1] - amount
            sngl_acc[1] = namount
            count = sngl_acc[2]
            count_key = max(count)+1
            sngl_acc[2][count_key] = f"Withdraw Amount {amount} With New Balance As {sngl_acc[1]} At {C_time()}"
        return namount 
def history():
    history = sngl_acc[2]
    for key, value in history.items():  
        fnl = f"{key}: {value}"
        print(fnl)
def open_accoiunt():
    while True:
            name = input("Enter Your Name: ")
            if name == ""  or name.isdigit() == True :
                print("Numbers And Empty IS not Acceptable")
            else:    
                def acc_num():
                    while True:
                        Num = random.randint(10000000, 99999999)
                        if Num not in Account:
                            return Num
                Account[acc_num()] = [name,00,{0:"Account Created"}]
                latest_acc = next(reversed(Account), None)
                done = f"Your Account Number Is {latest_acc} Owned By {name}"
                return done
def transfer():
        while True:
            try:
                trns_num = int(input("Enter the account number in which you want to transfer: "))
                trns_ammnt = int(input("Enter The Ammount: "))
            except ValueError:
                rtrn =  "Enter The Account Number/Amount"
                return rtrn
            if trns_num==account:
                print("Cannot transfer to Own Account")
            elif trns_ammnt <=0:
                print("Enter the Right Figure")
                return sngl_acc[1]
            elif trns_ammnt>sngl_acc[1]:
                print("You fucking thiefffff")
                return sngl_acc[1]
            else: 
                try:           
                    trns_acc = Account[trns_num]
                except KeyError :
                    error = "Enter Correct Account Number"
                    return error     
                acc_reduction = sngl_acc[1]- trns_ammnt
                sngl_acc[1] = acc_reduction
                acc_transfer = trns_acc[1] + trns_ammnt
                trns_acc[1] = acc_transfer
                sm_time = C_time()
                count = sngl_acc[2]
                count_key = max(count)+1
                sngl_acc[2][count_key] = f"'{trns_ammnt}' Ammout Transferd to {trns_num} at {sm_time} witn left balance {sngl_acc[1]}"
                count1 = trns_acc[2]
                count1_key = max(count1)+1
                trns_acc[2][count1_key] = f"{trns_ammnt} Amount Recived from {account} at {sm_time} witn new balance {trns_acc[1]}"
                print("Transfer Successful")
                return sngl_acc[1]
purpose = input("Ohh! Tell us Why Did you bother to come: \n A) Account  Exist \n B) Create New Account \n Enter.... : ")
if purpose.lower()== "a" or purpose.lower()=="account exist":
    try:
        account = int(input("Enter Your Account Number: "))
        sngl_acc = Account[account]
    except KeyError:
        print("Account does not exist.... \nEnter a Valid Number")
        sys.exit()
    except ValueError:
        print("Enter The Account Number (Only NUmbers Are Expected)")
        sys.exit()
    while True:
        menu = input("Reasone to login: \n 1. Withdraw \n 2. Deposit \n 3. Transfer \n 4. History \n 5. Exit Enter...: ")
        if menu=="1" or menu.lower()=="withdraw":
            print(f"new total = {withdraw()}")
        elif menu=="2" or menu.lower()=="deposit":
            print(f"new total = {deposit()}")
        elif menu=="3"or menu.lower()=="transfer": 
            print(f"Amount Left{transfer()}")
        elif menu=="4"or menu.lower()=="history":
            print(history())
        elif menu=="5"or menu.lower()=="exit":
            print(input("Enter to Exit...."))
            break
        else:
            print("Select from the optt")     
elif purpose.lower()== "b" or purpose.lower() == "create new account":
    print(open_accoiunt()) 
else:
    print("Enter From Givin Item")    
with open('data.pkl', 'wb') as file:
    pickle.dump(Account, file)    

