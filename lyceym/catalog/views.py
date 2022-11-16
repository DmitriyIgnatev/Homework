from django.shortcuts import render
from .models import Item


def item_list(request):
    items = Item.objects.published()
    context = {
        'items': items
    }
    return render(request, 'catalog.html', context)


def item_detail(req, pk):
    item = Item.objects.get_item(pk=pk)
    context = {
        'items': item
    }
    return render(req, 'catalog_item.html', context)
