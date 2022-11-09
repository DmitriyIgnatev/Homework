from django.shortcuts import render


def item_list(request):
    return render(request, 'catalog.html')


def item_detail(req, pk):
    return render(req, 'catalogitem.html', {'pk': pk})
