from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


def description(request):
    return render(request, 'about.html')


def description_new(req):
    url = reverse('about')
    return HttpResponseRedirect(url)
