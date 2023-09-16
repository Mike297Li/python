# use constant to store these three value, in case changed
CORRECTUSERNAME = 'Tim'
CORRECTPASSWORD = '12345'
MAXTRY = 3
userName = input("please enter username")
# check userName first time
if userName == CORRECTUSERNAME:
    print("==congratulation！==correct username====")
else:
    while userName != CORRECTUSERNAME:
        userName = input("incorrect user name,please enter correct username")
        # check userName again
        if userName == CORRECTUSERNAME:
            print("==congratulation！==correct username====")
password = input("please enter password")
if password == CORRECTPASSWORD:
    print("==congratulation！==correct password====")
else:
    count = 1
    while count <= MAXTRY:
        # try max time,still error password,exit
        if count == MAXTRY and password != CORRECTPASSWORD:
            print("sorry! you have already reached maximum of three attempts,please try later")
            break
        elif count < MAXTRY:
            password = input("incorrect password,please enter correct password")
            count += 1
            # check password again
            if password == CORRECTPASSWORD:
                print("==congratulation！==correct password====")
                break
