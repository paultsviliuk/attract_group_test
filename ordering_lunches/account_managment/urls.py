from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='ProductListByCategory'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]