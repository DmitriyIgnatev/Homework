from django.shortcuts import render, get_object_or_404
from .models import Item


def item_list(request):
    items = Item.objects.published()
    context = {
        'item': items
    }
    return render(request, 'catalog.html', context)


def item_detail(req, pk):
    item = [get_object_or_404(Item, pk=pk)]
    context = {
        'item': item,
    }
    return render(req, 'catalog_item.html', context)
