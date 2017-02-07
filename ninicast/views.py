# coding=utf-8
from random import randrange

from django.shortcuts import render, get_object_or_404
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from itssafe.models import itssafePosts
from itsnormal.models import itsNormalPosts
import datetime



def hello(request):
    items = []
#collect 1 item from each itssafe coloumn
    travel = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=1)[0]
    items.append(travel)

    food = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=2)[0]
    items.append(food)

    sport = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=3)[0]
    items.append(sport)


    healths = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=4)[0]
    items.append(healths)


    beauty = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=5)[0]
    items.append(beauty)


    sleep = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=6)[0]
    items.append(sleep)


    homeAndWork = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=7)[0]
    items.append(homeAndWork)


# collect 1 item from each itsnormal coloumn
    behaviors = itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID=1)[0]
    items.append(behaviors)


    growths = itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID=2)[0]
    items.append(growths)


    healths = itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID=3)[0]
    items.append(healths)


    newmoms = itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID=4)[0]
    items.append(newmoms)

    # اگر تعداد پست ها مضرب ۴ بود نتیجه 0 برمی گرداند  ( برای نمایش آخرین دیو )
    mymod = len(items) % 4

    context = {
        'items': items,
        'mod4':mymod,
    }
    return render(request, 'mainpage.html', context)
def googleWebmasterToolLink(request):
    return render(request,'googleab93e03628178ac3.html')

class ItsSafeSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return itssafePosts.objects.all()

    def lastmod(self, obj):
        return obj.publication_date

class ItsNormalSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return itsNormalPosts.objects.all()
    def lastmod(self, obj):
        return obj.publication_date

class mainPagesSitemap(Sitemap):
    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'daily'

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse(obj)



def showFeedPost(request, id=None):
    intId= int(id)
    reservedListIds=[]
    reservedListIds.append(int(id))
    # if id number>3 then kind of maqalat is itsnormal else itssafe
    if (int(id) > 3):
        mylist = itsNormalPosts.objects.order_by('publication_date')[:3]  # 3 number must sync with feeds.py
        postURL = mylist[intId - 4].get_absolute_url # 4 number must sync with feeds.py
        feedItemClickedItem = mylist[intId - 4]# 4 number must sync with feeds.py
        #
        items = itsNormalPosts.objects.filter(status=1)
        counter = 0
        for item in items:
            if (int(item.id) == feedItemClickedItem.id):
                idLocation = counter
                postURL = get_object_or_404(itsNormalPosts, id=feedItemClickedItem.id)
                catagoryName = item.categoryName
                catagoryCode = item.categoryCode
    else:
        mylist = itssafePosts.objects.order_by('publication_date')[:3]  # 3 number mux sync with feeds.py
        postURL = mylist[intId-1].get_absolute_url
        feedItemClickedItem= mylist[intId-1]
    # پیدا کردن آیدی پست قبلی و پست بعدی تا در دکمه های بک و نکست استفاده بشن
        items = itssafePosts.objects.filter(status=1)
        counter = 0
        for item in items:
            if (int(item.id)==feedItemClickedItem.id):
                idLocation=counter
                postURL = get_object_or_404(itssafePosts, id=feedItemClickedItem.id)
                catagoryName=item.categoryName
                catagoryCode=item.categoryCode
            counter+=1

    if (idLocation==0):
        prevID = -1
    else:
        prevID = int(items[idLocation - 1].id)

    # *********next Id*********

    if (idLocation == len(items)-1):
        nextID = -1
    else:
        nextID = int(items[idLocation + 1].id)
        # ************* same posts*****************
        # ***choose other post 1
        while True:
            random1 = randrange(0, len(items) - 1)
            if (random1 not in reservedListIds):  # اگه این پست تو لیست نمایش ها نبود قبولش میکنیم و میریم به مرحله بعد
                reservedListIds.append(random1)
                break
        # ***choose other post 2
        while True:
            random2 = randrange(0, len(items) - 1)
            if (random2 not in reservedListIds):  # اگه این پست تو لیست نمایش ها نبود قبولش میکنیم و میریم به مرحله بعد
                reservedListIds.append(random2)
                break
        # ***choose other post 3
        while True:
            random3 = randrange(0, len(items) - 1)
            if (random3 not in reservedListIds):  # اگه این پست تو لیست نمایش ها نبود قبولش میکنیم و میریم به مرحله بعد
                # tempId.append(random3)
                break

    # اگر تعداد پست ها مضرب ۴ بود نتیجه 0 برمی گرداند  ( برای نمایش آخرین دیو )
    mymod = len(items) % 4


    context = {
        'post': postURL,
        'prevID': prevID,
        'nextID': nextID,
        'catagoryName': catagoryName,
        'catagoryCode': catagoryCode,
        'samePost1': items[random1],
        'samePost2': items[random2],
        'samePost3': items[random3],
         'mod4':mymod,
    }

    return render(request, 'post.html',context)

