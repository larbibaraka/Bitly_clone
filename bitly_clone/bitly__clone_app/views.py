from .models import UrlShort
from django.shortcuts import render,get_object_or_404,get_list_or_404,Http404,redirect,HttpResponse
from .forms import UrlShortForm

# CRUD IMPORTS

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.


def home(request):
    urls_data=UrlShort.objects.order_by('-nb_access')[:10]

    return render(request,'bitly__clone_app/home.html',locals())



def add_new_url(request):

    if request.method == "POST":
        my_form=UrlShortForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect(home)
        else:
            print (my_form)
    else:
        my_form=UrlShortForm()

    return render(request,'bitly__clone_app/new.html',{'form': my_form})


def redirection(request,url_code):

    bitly_clone=get_object_or_404(UrlShort,url_code=url_code)
    bitly_clone.nb_access=bitly_clone.nb_access+1
    bitly_clone.save()

    return redirect(bitly_clone.user_url, permanent=True)



class CreateUrl(CreateView):
    model = UrlShort
    template_name = "bitly__clone_app/new.html"
    form_class = UrlShortForm
    success_url = reverse_lazy('index of home')#you give the name of the url


