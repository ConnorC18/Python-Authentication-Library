import base64
import smtplib
import ssl
import random
import fileinput
global loggedIn
loggedIn = False


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


class user:
    def __init__(self,username,password,email,question,answer):
        self.username = username
        self.password = password
        self.email = email
        self.question = question
        self.answer = answer


def checkPassword(password):
    flag = 0
    errors = []
    if sum(1 for character in password if character.isdigit()) > 0:
        flag += 1
    else:
        flag -= 1
        errors.append("You must have at least 1 digit in your password")
    if len(password) >= 6:
        flag += 1
    else:
        flag -= 1
        errors.append("Your password must be at least 6 characters long")
    letters = set(password)
    lower = any(letter.islower() for letter in letters)
    upper = any(letter.isupper() for letter in letters)
    if not lower:
        flag -= 1
        errors.append("Your password must contain a lower case letter")
    else:
        flag += 1
    if not upper:
        flag -= 1
        errors.append("Your password must contain a upper case letter")
    else:
        flag += 1
    if set('[~!@#$%^&*()_+{}":;\']+$').intersection(password):
        flag += 1
    else:
        flag -= 1
        errors.append('Your password must contain a special character')
    ret = []
    if flag >= 4:
        ret.append(True)
        ret.append(errors)
        return ret
    else:
        ret.append(False)
        ret.append(errors)
        return ret

def getUsers():
    users = open('users.txt','r')
    global userList
    userList = []
    for line in users:
        line.replace('\n','')
        line = line.split('|')
        userList.append(user(line[0],line[1],line[2],line[3],line[4]))
    users.close()
    return userList


def passwordReset():
    email = input("Please enter the email of the account you want to reset: ")

    userList = getUsers()
    index = -1
    for i in range(0,len(userList)-1):
        if userList[i].email == email:
            index = i
    if index == -1:
        print("Email doesnt exist!")
        passwordReset()



    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "emailpythonexample@gmail.com"
    receiver_email = email
    password = "SupportMailExample"
    resetCode = random.randint(1000,9999)
    message = """\
    Subject: Password Reset

    Please Enter this code in python """+str(resetCode)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print("Password reset sent! Make sure to check your spam folder.")

    code = input("Please enter the reset code: ")
    while str(code) != str(resetCode):
        print("Incorrect code!")
        code = input("Please enter the reset code: ")


    newPassword = input("Please enter the new password: ")
    newPasswordConfirm = input("Please re-enter the new password: ")
    flag = checkPassword(newPassword)
    while newPassword != newPasswordConfirm or flag[0] is False:
        newPassword = input("Please enter the new password")
        newPasswordConfirm = input("Please re-enter the new password: ")
        flag = checkPassword(newPassword)

    text_to_search = userList[index].password

    with fileinput.FileInput('users.txt', inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(text_to_search, encode(newPassword,newPassword)), end='')

    print("Password Reset!")


def signUp():
    username = input("Please Enter a username: ")
    userList = getUsers()
    for user in userList:
        if (user.username).lower() == username.lower():
            print("Error Username Taken!")
            signUp()
    password = input("Please Enter a password: ")
    passwordCheck = checkPassword(password)
    if passwordCheck[0]:
        print("Valid")
    else:
        print("Invalid Password\n")
        print("Errors:")
        for error in passwordCheck[1]:
            print(error)
        print("\n")
        signUp()
    email = ""
    checkMail = False
    temp = False
    email = input("Please enter your email")
    while checkMail == False:
        temp = False
        for user in userList:
            if (user.email).lower() == email.lower():
                temp = True
        if temp == True or "@" not in email:
            if temp == True:
                print("in use")
            elif "@" not in email:
                print("@ not in")
            else:
                print("WTF")
            print("Invalid email or email is already in use")
            email = input("Please enter your email")
        else:
            checkMail = True

    question = 0
    while not (int(question) >= 1 and int(question) <= 16):
        question = input("""Please Select a Security question
        1: What was your childhood nickname? 
        2: In what city did you meet your spouse/significant other?
        3: What is the name of your favorite childhood friend? 
        4: What street did you live on in primary school?
        5: What is your oldest sibling’s birthday month and year? (e.g., January 1900) 
        6: What is the middle name of your youngest child/sibling?
        7: What is your oldest sibling's middle name?
        8: What was the name of your first stuffed animal?
        9: In what city or town did your mother and father meet? 
        10: Where were you when you had your first kiss? 
        11: What is the first name of the boy or girl that you first kissed?
        12: In what city does your nearest sibling live? 
        13: What is your youngest brother’s birthday month and year? (e.g., January 1900) 
        14: In what city or town was your first job?
        15: What is the name of the place your wedding reception was held?
        16: What is the name of a college you applied to but didn't attend?
        """)
        try:
            if not (int(question) >= 1 and int(question) <= 16):
                print("Invalid number")
        except ValueError:
            question = 0
            print("Invalid Number")


    questionList = ["What was your childhood nickname?","In what city did you meet your spouse/significant other?","What is the name of your favorite childhood friend?","What street did you live on in primary school?","What is your oldest sibling’s birthday month and year? (e.g., January 1900),What is the middle name of your youngest child/sibling?","What is your oldest sibling's middle name?","What was the name of your first stuffed animal?","In what city or town did your mother and father meet?","Where were you when you had your first kiss?","11: What is the first name of the boy or girl that you first kissed?","In what city does your nearest sibling live?","13: What is your youngest brother’s birthday month and year? (e.g., January 1900),In what city or town was your first job?","What is the name of the place your wedding reception was held?","What is the name of a college you applied to but didn't attend?"]
    print(questionList[int(question)-1])
    answer = input("Answer: ")
    password = encode(password,password)
    user = open("users.txt","a")
    string = username+"|"+password+"|"+email+"|"+questionList[int(question)-1]+"|"+answer+"\n"
    user.write(str(string))


def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    getUsers()
    correct = False
    try:
        for user in userList:
            if (user.username).lower() == username.lower() and decode(password,user.password) == password:
                correct = True
                break
        if correct:
            loggedIn = True
        else:
            print("Error: Incorrect password or username")
    except IndexError:
        print("Error: No accounts exist.")


def checkLoggedIn():
    if loggedIn:
        return True
    else:
        return False