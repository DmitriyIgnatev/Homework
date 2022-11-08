from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'homepage.html')


def home_new(req):
    redirect_url = reverse('homepage')
    return HttpResponseRedirect(redirect_url)
