from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

array = []


def search(request):
    form = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST or None)
        if form.is_valid():
            # print(form.data.get('url'))
            url = form.cleaned_data['url']
            array.append(url)
            form = SearchForm()
        print(array)
    return render(request, 'index.html', {'form': form})


def counter(request):
    context = {
        'facebook': [1, 2, 3, 4],
        'google': [1, 2, 3, 4,5,6,7,8],
    }
    return JsonResponse(context, safe=False)
