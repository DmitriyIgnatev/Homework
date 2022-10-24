from django.shortcuts import HttpResponse


def description(req):
    return HttpResponse('О проекте')
