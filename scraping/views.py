from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import *


def search(request):
    if request.method == "POST":
        url = request.POST['url']
        UrlStore.objects.create(url=url)
        return render(request, 'GUI.html')
    return render(request, 'GUI.html')


def clear(request):
    if request.method == "POST":
        UrlStore.objects.all().delete()
        return render(request, 'GUI.html')


def counter(request):
    context = {
        'facebook': [1, 2, 3, 4],
        'google': [1, 2, 3,4,5,6,7,8],
    }
    return JsonResponse(context, safe=False)
