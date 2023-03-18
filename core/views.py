from django.http import HttpResponse


def my_path(request):
    return HttpResponse('<h1>Hello World!!!</h1>')
