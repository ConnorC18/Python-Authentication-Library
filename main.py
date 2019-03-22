from loginSystem import *


signUp()
login()
if checkLoggedIn():
    passwordReset()
    login()
else:
    print("Not Logged in")




