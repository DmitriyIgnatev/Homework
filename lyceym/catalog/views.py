from django.shortcuts import HttpResponse


def item_list(req):
    return HttpResponse('Список элементов')


def item_detail(req, pk):
    print(pk)
    return HttpResponse(f'Подробно элемент {pk}')
