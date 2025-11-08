from cryptography.fernet import Fernet

psw=input("What is the password?\n")



def use_key():
    file = open("key.key","rb")
    key=file.read()
    file.close()
    return key


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
           data = line.rstrip()
           user, passw = data.split("|",1)

           print("User:",user,"| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name= input("Account Name: ")
    pwd= input("Account Password: ")
    with open('password.txt','a') as f:
        f.write(name + " | "+ fer.encrypt(pwd.encode()).decode() + "\n")


key=use_key()
fer = Fernet(key)

while True:
    mode=input("Add or View password(s)? Or q to quit\n")
    mode.lower()

    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid")
        continue


