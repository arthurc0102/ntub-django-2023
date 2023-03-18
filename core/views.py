from django.http import HttpResponse


def my_path(request):
    name = request.GET.get('name', 'Unknown')
    return HttpResponse(f'<h1>Hello World {name}!!!</h1>')
