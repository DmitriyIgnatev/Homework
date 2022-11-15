from django.shortcuts import render
from catalog.models import Item


def home(request):
    item = Item.objects.main_published()
    context = {
        'item': item
    }
    return render(request, 'homepage.html', context)
