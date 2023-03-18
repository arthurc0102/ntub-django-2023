from django.shortcuts import render


def my_path(request):
    name = request.POST.get('name', 'Unknown')
    return render(request, 'my_path.html', {'name': name})
