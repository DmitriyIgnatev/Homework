from django.shortcuts import render
from catalog.models import Item


def home(request):
    items = Item.objects.published().filter(is_on_main=True).order_by('name')
    context = {
        'items': items,
    }
    return render(request, 'homepage.html', context)
