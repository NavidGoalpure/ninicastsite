# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from itssafe.models import itssafePosts
from itsnormal.models import itsNormalPosts
from itertools import chain

class LatestItssafeFeed(Feed):
    title = "نجوای جدید سلامت در دوران بارداری"
    link = "/itssafe/"
    description = "آپدیت و اضافه کردن مطالب جدید در ارتباط با سلامت مادران باردار"

    def items(self):
        return chain(itssafePosts.objects.order_by('publication_date')[:5] , itsNormalPosts.objects.order_by('publication_date')[:5])

    def item_title(self, item):
        return item.titr

    def item_description(self, item):
        return item.desc