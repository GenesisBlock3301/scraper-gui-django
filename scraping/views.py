from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import *
from bs4 import BeautifulSoup
import html5lib
html5parser = html5lib.HTMLParser(strict=True)


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


def test(request):
    if request.method == "POST":
        text = request.POST['text']
        html5parser = html5lib.HTMLParser(strict=True)
        try:
            ans_text = html5parser.parse(text)
        except:
            ans_text = False
        if ans_text:
            return HttpResponse(text)
        else:
            return HttpResponse("Error")
    return render(request,'index.html')
