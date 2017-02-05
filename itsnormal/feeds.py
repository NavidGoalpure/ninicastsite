# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from itsnormal.models import itsNormalPosts

class LatestItsnormalFeed(Feed):
    title = "نجوای جدید سلامت مادر و نوزاد"
    link = "/itsnormal/"
    description = "آپدیت و اضافه کردن مطالب جدید در ارتباط با سلامت مادر و نوزاد"

    def items(self):
        return itsNormalPosts.objects.order_by('publication_date')[:5]

    def item_title(self, item):
        return item.titr

    def item_description(self, item):
        return item.desc