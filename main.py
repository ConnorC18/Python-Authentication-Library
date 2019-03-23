from loginSystem import *

print(signUp())                 # Will return True or the error message thrown by the function
print(login())                  # Will return True or "incorrectinfo" or "noaccount" depending on the error.
print(sessionInfo["username"])  # Will return the current logged in users, username
print(logout())                 # Will return True or "notloggedin"
print(passwordReset())          # Will return True or "noemail" or "wrongsecurityquestionanswer" 





