from django.conf.urls import handler404, handler500
from django.shortcuts import render


def handler404(request, exception):

    return render(request, 'errors/404.html', status=404)


def handler500(request, *args, **argv):
    return render(request, 'errors/500.html', status=500)