from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
# <-----Imports----->
import requests
from bs4 import BeautifulSoup as bs
import json
import math
import pandas as pd
import time

URLS = []

JSON_PATH = ""
XLSX_PATH = ""



def google_search(request):
    if request.method == "POST":
        status = False
        try:
            url = request.POST['url']
            Facebook.objects.create(url=url)
        except:
            status = True
        return render(request, 'Google_GUI.html',{'status':status})
        
    return render(request, 'Google_GUI.html')


# <-----Functions----->
def write_json(name,data):
    print("\n>>>>>>>>>>>>> Writing JSON File\n")
    with open(name + ".json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        
def write_xlsx(name,data):
    print("\n>>>>>>>>>>>>> Writing XLSX File\n")
    with open(name + ".json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

def getInfo(url):
    res=requests.get(url)
    soup = bs(res.content, 'lxml')
    data = json.loads(soup.select_one('[type="application/ld+json"]').text)[0]
    return data

def addItems(data):
    result = []    
    # <----- Get Review Data ----->
    for item in data['review']:
        review = { 
                  'Author' : item["author"]["name"],
                  'Headline': item['headline'] ,
                  'Ranking': item['reviewRating']['ratingValue'],
                  'Review': item['reviewBody'],
                  'ReviewDate': item['datePublished']
                }
        result.append(review)
    return result




def pageCounter(URLS):
    
    # <-----Code----->
    # <----- Loop through all URLS ----->
    dic = {}
    for url in URLS:
        print(">>>>>>>>>>>>> Visiting URL: {}".format(url))
        url = url + '?page={}'
        results = []
        data = {
            "ID" : {},
            "URL" : {},
            "Name" : {},
            "Data" : {}
        }
        print(">>>>>>>>>>>>> Scraping Page: {}".format(1))
        a_data = getInfo(url.format(1))
        data["ID"] = a_data["@id"]
        data["URL"] = a_data["url"]
        data["Name"] = a_data["name"]
        results.append(addItems(a_data))
        totalReviews = int(a_data['aggregateRating']['reviewCount'])
        reviewsPerPage = len(a_data['review'])
        totalPages = math.ceil(totalReviews/reviewsPerPage)
        dic[url] = []
        if totalPages > 1:
            dic[url].extend([x for x in range(1,totalPages+1)])
            print(dic)
            for page in range(2, totalPages + 1):
                print(">>>>>>>>>>>>> Scraping Page: {}".format(page))
                a_data = getInfo(url.format(page))
                results.append(addItems(a_data))



        final = [item for result in results for item in result]

        data["Data"] = final
        
        # <----- Writing JSON ----->
        write_json(data["Name"],data)
        
        df = pd.DataFrame(data)
        df.head()
        
        print("\n>>>>>>>>>>>>> Writing XLSX File\n")
        df.to_excel(data["Name"] + '.xlsx')
        
        
    print(">>>>>>>>>>>>> Completed successfully !!!")
    return dic

# URLS = []

def google_counter(request):
    # print("Before",URLS)
    for i in GOOGLE.objects.all():
        print(type(i))
        URLS.append(str(i))
    print(URLS)
    context = pageCounter(list(set(URLS)))
    print(context)
    return JsonResponse(context, safe=False)

def google_clear(request):
    if request.method == "POST":
        GOOGLE.objects.all().delete()
        return render(request, 'Google_GUI.html')
