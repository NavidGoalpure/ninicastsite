# -*- coding: utf-8 -*-from django.conf.urls import urlfrom itssafe.feeds import LatestItssafeFeedfrom . import viewsurlpatterns = [    url(r'^safe1', views.itssafeTravel, name='travel'),    url(r'^safe2', views.itssafeFood, name='food'),    url(r'^safe3', views.itssafeSport, name='sport'),    url(r'^safe4', views.itssafeHealths, name='healths'),    url(r'^safe5', views.itssafeBeauty, name='beauty'),    url(r'^safe6', views.itssafeSleep, name='sleep'),    url(r'^safe7', views.itssafeHomeAndWork, name='homeAndWork'),    # url(r'^safe[0-9]{1,3}', views.itssafe, name='base'),    url(r'^(?P<id>[0-9]{1,3})$', views.showSafePost, name='showpost'),    # feeds urls    url(r'^latest/(?P<id>[0-9]{1,3})$', views.showSafePost, name='showpost'),    url(r'^latest/feed/$', LatestItssafeFeed()),    #    url(r'^', views.itssafe, name='itssafeBase'),]