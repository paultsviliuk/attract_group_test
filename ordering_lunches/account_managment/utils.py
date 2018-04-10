import secrets
import string
from string import ascii_letters
from random import choice

def passGenerator():
    return ''.join(choice(ascii_letters) for i in range(10))

#def passwordGen(self):
 #   alphabet = string.ascii_letters + string.digits
  #  password = ''.join(secrets.choice(alphabet) for i in range(10))
   # return password
