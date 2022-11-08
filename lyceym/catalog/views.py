from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from django.urls import reverse


def item_list(request):
    return render(request, 'catalog.html')


def item_detail(req, pk):
    return HttpResponse(f'Подробно элемент {pk}')


def catalog_new(req):
    redirect_url = reverse('catalog')
    return HttpResponseRedirect(redirect_url)
