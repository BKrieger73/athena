from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import logout

from login.models import NewUser, Course, Lesson, Progress


def index(request, username):
    if request.user.is_authenticated:
        return render(request, 'homepage/index.html',{"UserName":request.user.username})
    else:
        return HttpResponseRedirect(reverse('login:index',args = tuple()))
    

def logoutuser(request):
    #return render(request, 'login/index.html',{})
    return HttpResponseRedirect(reverse('login:index'))
    #return HttpResponse("ahha")
    #return HttpResponse("ahha")
    #logout(request)
