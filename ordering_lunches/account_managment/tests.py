from django.test import TestCase
import requests,json


# Create your tests here.
def TestAddUser(name,surname,email,password,telephone):
    dic={
        "name" : name,
        "surname" : surname,
        "email" : email,
        "password" : password,
        "telephone" : telephone
         }
    r=requests.post("http://127.0.0.1:8000/account_managment/addUser/",data=json.dumps(dic))
    print(r.text)


def TestAuthorizeUser(email,password,telephone):
    dic = {
        "email": email,
        "password": password,
        "telephone": telephone
    }
    r = requests.post("http://127.0.0.1:8000/account_managment/authorizeUser/",data=json.dumps(dic))
    print(r.text)


TestAddUser(name="Paul",surname="Tsvilyuk",email="paultsvilyuk@gmail.com",password="asddsa",telephone="380932477099")
#TestAuthorizeUser(email="paultsvilyuk@gmail.com",password="asddsa",telephone="380932477099")
