# coding=utf-8
from django.shortcuts import render , get_object_or_404
from .models import itssafePosts
from django.views.decorators.cache import cache_page


def itssafe(request):

    travel= itssafePosts.objects.filter(status=1).filter(categoryName__categoryID =1)
    maxnumber= len(travel)

    food= itssafePosts.objects.filter(status=1).filter(categoryName__categoryID =2)
    if maxnumber<len(food):
        maxnumber=len(food)

    sport= itssafePosts.objects.filter(status=1).filter(categoryName__categoryID =3)
    if maxnumber<len(sport):
        maxnumber=len(sport)

    healths= itssafePosts.objects.filter(status=1).filter(categoryName__categoryID =4)
    if maxnumber<len(healths):
        maxnumber=len(healths)

    beauty= itssafePosts.objects.filter(status=1).filter(categoryName__categoryID =5)
    if maxnumber<len(beauty):
        maxnumber=len(beauty)

    sleep= itssafePosts.objects.filter(status=1).filter(categoryName__categoryID =6)
    if maxnumber<len(sleep):
        maxnumber=len(sleep)

    homeAndWork= itssafePosts.objects.filter(status=1).filter(categoryName__categoryID =7)
    if maxnumber<len(homeAndWork):
        maxnumber=len(homeAndWork)

    # make a dic with sum all of them
    items=[]
    y=0
    while (y<= maxnumber):
        if  y<travel.count():
            items.append(travel[y])
        if y<food.count():
            items.append(food[y])
        if y<sport.count():
            items.append(sport[y])
        if y<healths.count():
            items.append(healths[y])
        if y<beauty.count():
            items.append(beauty[y])
        if y<sleep.count():
            items.append(sleep[y])
        if y<homeAndWork.count():
            items.append(homeAndWork[y])
        y+=1
    context ={
        'items':items,
    }
    return render(request,'itssafe.html',context)


def itssafeTravel(request):
    items = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=1)
    context ={
        'items':items,
    }
    return render(request,'itssafe.html',context)


def itssafeFood(request):
    items = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=2)
    context ={
        'items':items,
    }
    return render(request,'itssafe.html',context)


def itssafeSport(request):
    items = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=3)
    context ={
        'items':items,
    }
    return render(request,'itssafe.html',context)


def itssafeHealths(request):
    items = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=4)
    context ={
        'items':items,
    }
    return render(request,'itssafe.html',context)


def itssafeBeauty(request):
    items = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=5)
    context ={
        'items':items,
    }
    return render(request,'itssafe.html',context)


def itssafeSleep(request):
    items = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=6)
    context ={
        'items':items,
    }
    return render(request,'itssafe.html',context)


def itssafeHomeAndWork(request):
    items = itssafePosts.objects.filter(status=1).filter(categoryName__categoryID=7)
    context ={
        'items':items,
    }
    return render(request,'itssafe.html',context)


def showSafePost(request, id=None):
    safePost = get_object_or_404(itssafePosts,id =id)

    # پیدا کردن آیدی پست قبلی و پست بعدی تا در دکمه های بک و نکست استفاده بشن
    items = itssafePosts.objects.filter(status=1)
    counter = 0
    for item in items:
        if (int(item.id)==int(id)):
            idLocation=counter
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

    context = {
        'post': safePost,
        'prevID': prevID,
        'nextID': nextID,
        'catagoryName': catagoryName,
        'catagoryCode': catagoryCode,
    }

    return render(request, 'post.html',context)



