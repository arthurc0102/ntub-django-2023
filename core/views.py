from django.http import HttpResponse


def my_path(request):
    name = request.GET['name']
    return HttpResponse(f'<h1>Hello World {name}!!!</h1>')
