from django.http import HttpResponse


def my_path(request):
    name = request.GET.get('name', 'Unknown')
    return HttpResponse(f'<form method="GET"><input type="text" name="name"><input type="submit" value="send"></form><h1>Hello World {name}!!!</h1>')
