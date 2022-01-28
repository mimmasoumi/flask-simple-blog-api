
from flask import session


def check_password(pass1, pass2):
    if len(pass1) < 4 or len(pass2) < 4:
        return "password lenght is low."
    elif pass1 != pass2:
        return "passwords not equal."
    elif pass1 == pass2:
        return True
    else:
        return False

def check_login():
    login = session.get("logged_in")
    if login:
        if login == True:
            return True
    else:
        return False
    
    return False

