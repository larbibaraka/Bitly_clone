from django.conf.urls import url
from django.views.generic import ListView
from .models import UrlShort


from . import views

urlpatterns=[

    #index of my website
    #url(r'^$',views.home,name='index of home'),
    url(r'^$',ListView.as_view(
        model=UrlShort,
        context_object_name="urls_data",
        template_name="bitly__clone_app/home.html"
    ),name="index of home"),
    #url(r'^anu/$',views.add_new_url,name='add new url'),
    url(r'^anu/$',views.CreateUrl.as_view(),name='add new url'),
    url(r'^(?P<url_code>\w{6})/$',views.redirection,name='redirection view'),



]




