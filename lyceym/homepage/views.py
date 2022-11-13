from django.shortcuts import render
from catalog.models import Item


def home(request):
    item = Item.objects.filter(is_on_main=True)
    context = {
        'item': item
    }
    return render(request, 'homepage.html', context)
