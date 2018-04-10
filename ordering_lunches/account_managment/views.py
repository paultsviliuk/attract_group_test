from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, Http404
from .models import User, UserTokken
from . import generationCodes
import json
import requests


# Create your views here.
users=User.objects
tokkens = UserTokken.objects

def getUsers(request):
    return HttpResponse(users)


def getUserInfo(request,tokken):
    try:
        tokken=tokkens.get(user_tokken=tokken)
        user_info={'name':tokken.user.name,
               'surname':tokken.user.surname,
               'email':tokken.user.email,
                'telephone':tokken.user.telephone
               }
        json_response=JsonResponse(user_info)
        return json_response

    except :
        return HttpResponseBadRequest("Illegal tokken")


def addUser(request):
    if request.method=='POST':
        request_info=str(request.body,'utf-8')
        user_info=json.loads(request_info)
        try:
            name=user_info['name']
            surname=user_info['surname']
            email=user_info['email']
            password=user_info['password']
            telephone=int(user_info['telephone'])

        except :
            return HttpResponseBadRequest("Illegal arguments")


        if users.filter(email=email).count()!=0:
            return HttpResponseBadRequest("this email is in use")
        if users.filter(telephone=telephone).count()!=0:
            return HttpResponseBadRequest("this phone is in use")


        try:
            u_count=users.all().count()
            if u_count>0:
                new_user=User(id=users.all()[u_count-1].id+1,name=name,surname=surname,email=email,password=password,telephone=telephone)
                tokken=generationCodes.makeTokken()
                new_user.save()
                new_user_tokken=UserTokken(tokken,new_user.id)
                new_user_tokken.save()
                dic={'tokken':tokken}
                json_response=JsonResponse(dic)
                return json_response
            else:
                new_user = User(id=0, name=name, surname=surname, email=email, password=password, telephone=telephone)
                tokken = generationCodes.makeTokken()
                new_user.save()
                new_user_tokken = UserTokken(tokken, new_user.id)
                new_user_tokken.save()
                dic = {'tokken': tokken}
                json_response = JsonResponse(dic)
                return json_response


        except :
            return HttpResponseBadRequest("Illegal arguments")


    else:
        return Http404("Illegal method")



def authorizeUser(request):
    if request.method=='POST':
        request_info = str(request.body, 'utf-8')
        user_info = json.loads(request_info)
        try:
            telephone=user_info['telephone']
            password=user_info['password']
            email=user_info['email']
            if telephone!='':
                user=users.get(telephone=telephone,password=password)
                tokken=tokkens.get(user=user)
                dic = {'tokken': tokken.user_tokken}
                json_response = JsonResponse(dic)
                return json_response
            if email!='':
                user = users.get(email=email, password=password)
                tokken = tokkens.get(user=user)
                dic = {'tokken': tokken.user_tokken}
                json_response = JsonResponse(dic)
                return json_response
            return HttpResponseBadRequest("Illegal arguments")
        except BaseException:
            return HttpResponseBadRequest("Illegal arguments")

    else:
        return Http404("Illegal method")