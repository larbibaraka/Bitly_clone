from django.conf.urls import url


from . import views

urlpatterns=[

    #index of my website
    url(r'^$',views.home,name='index of home'),
    url(r'^anu/$',views.add_new_url,name='add new url'),
    url(r'^(?P<url_code>\w{6})/$',views.redirection,name='redirection view'),



]




