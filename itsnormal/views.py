# coding=utf-8
from django.shortcuts import render , get_object_or_404
from .models import itsNormalPosts
from random import randrange
def itsnormal(request):

    behaviors= itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID =1)
    maxnumber= len(behaviors)

    growths= itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID =2)
    if maxnumber<len(growths):
        maxnumber=len(growths)

    healths= itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID =3)
    if maxnumber<len(healths):
        maxnumber=len(healths)

    newmoms= itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID =4)
    if maxnumber<len(newmoms):
        maxnumber=len(newmoms)
    # make a dic with sum all of them
    items=[]
    y=0
    while (y<= maxnumber):
        if  y<behaviors.count():
            items.append(behaviors[y])
        if y<growths.count():
            items.append(growths[y])
        if y<healths.count():
            items.append(healths[y])
        if y<newmoms.count():
            items.append(newmoms[y])
        y+=1
    context ={
        'items':items,
    }
    return render(request,'itsnormal.html',context)


def itsnormalBehaviors(request):
    items = itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID=1)
    context ={
        'items':items,
    }
    return render(request,'itsnormal.html',context)


def itsnormalGrowths(request):
    items = itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID=2)
    context ={
        'items':items,
    }
    return render(request,'itsnormal.html',context)


def itsnormalHealths(request):
    items = itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID=3)
    context ={
        'items':items,
    }
    return render(request,'itsnormal.html',context)


def itsnormalNewmoms(request):
    items = itsNormalPosts.objects.filter(status=1).filter(categoryName__categoryID=4)
    context ={
        'items':items,
    }
    return render(request,'itsnormal.html',context)


def showNormalPost(request, id=None):
    reservedListIds=[]
    reservedListIds.append(int(id))
    normalPost = get_object_or_404(itsNormalPosts,id =id)

    # پیدا کردن آیدی پست قبلی و پست بعدی تا در دکمه های بک و نکست استفاده بشن
    items = itsNormalPosts.objects.filter(status=1)
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

#************* same posts*****************
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
                #tempId.append(random3)
                break


                # اگر تعداد پست ها مضرب ۴ بود نتیجه 0 برمی گرداند  ( برای نمایش آخرین دیو )
    mymod = len(items) % 4
    context = {
        'post': normalPost,
        'prevID': prevID,
        'nextID': nextID,
        'catagoryName': catagoryName,
        'catagoryCode': catagoryCode,
        'samePost1': items[random1],
        'samePost2': items[random2],
        'samePost3': items[random3],
        'mod4': mymod,
    }

    return render(request, 'post.html',context)
