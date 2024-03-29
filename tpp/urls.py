"""tpp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from tppbot import views
from hIncruit import views
from hIncruit import announce
from hIncruit import stocks

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('keyboard',views.keyboard),
    #path('message',views.answer),
    #path('todaysmenu',views.todaysmenu),
    #path('showUser',views.showUser, name='showUser'),
    #path('addUser',views.addUser),
    #path('list', views.list),
    #path('topfive', views.topFivePlace)
    path('question', views.Question),
    path('makeq', views.makeQuestion),
    path('result', views.result),
    path('makeA',announce.makeAnnouncement),
    path('makeAD',announce.makeAnnouncementDetail),
    path('AList',announce.announcementList),
    #path('Stock',stocks.StockData),
    path('StockSkill', stocks.StockSkill)
]

