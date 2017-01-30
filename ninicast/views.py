# coding=utf-8
from django.shortcuts import render
from django.contrib.sitemaps import Sitemap
from itssafe.models import itssafePosts
from itsnormal.models import itsNormalPosts



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


    context = {
        'items': items,
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
