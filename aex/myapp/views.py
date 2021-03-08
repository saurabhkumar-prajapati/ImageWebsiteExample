from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.views.generic import TemplateView

from .forms import Add
from .models import Newuser
# Create your views here.
#displays events
class Home(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Newuser.objects.all()


        return context

    template_name = 'myapp/home.html'

#def home(request): #function for home page
    #images= Newuser.objects.all()
    #return render(request, "myapp/home.html",{ 'images':'images'})

#for adding events
def add_show(request):

    if request.method == 'POST':
        fm=Add(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm=Add()
    else:
        fm=Add()
    return render(request,"myapp/createview.html",{'form':fm,})

#for deleting event
def delete_event(request,id):
    events=Newuser.objects.all()

    event =Newuser.objects.get(pk=id)
    if request.method == 'POST':
        event.delete()
        return HttpResponseRedirect("/")
    return render(request,"myapp/home.html",{'events':events})

