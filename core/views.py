from django.shortcuts import render


def my_path(request):
    name = request.GET.get('name', 'Unknown')
    return render(request, 'my_path.html', {'name': name})
