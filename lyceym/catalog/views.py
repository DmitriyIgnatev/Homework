from django.shortcuts import HttpResponse, render


def item_list(request):
    return render(request, 'catalog.html')


def item_detail(req, pk):
    return HttpResponse(f'Подробно элемент {pk}')
