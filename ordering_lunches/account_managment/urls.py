from django.conf.urls import url
from . import views


urlpatterns = [
    # : /account_managment/addUser/
    url(r'^addUser/$', views.addUser, name='addUser'),
    # : /account_managment/authorizeUser/
    url(r'^authorizeUser/$', views.authorizeUser, name='authorizeUser'),
]