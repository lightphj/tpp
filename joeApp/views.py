from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mapCrawler(request):
    msg = 'Django로 Crawler를 만들어 봅시다.'
    return render(request, 'index.html', {'message': msg})
    #return HttpResponse("Django로 Crawler를 만들어 봅시다.")

def mapView(request):
    msg = 'Django로 Crawler를 만들어 봅시다.'
    return render(request, 'mapView.html', {'message': msg})
    #return HttpResponse("Django로 Crawler를 만들어 봅시다.")
