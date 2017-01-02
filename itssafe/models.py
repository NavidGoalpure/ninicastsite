# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import DateField
from django.core.urlresolvers import reverse
from django.conf import settings
import os.path

class itssafeCategories(models.Model):
    categoryName = models.CharField(max_length=30)
    categoryID = models.PositiveSmallIntegerField(unique=True,)
    def __unicode__(self):
        return self.categoryName

class itssafePosts(models.Model):
    titr = models.CharField(max_length=100)
    desc = models.TextField()

    ageRangeStart = models.SmallIntegerField(default=-1000)
    ageRangeEnd = models.SmallIntegerField(default=0)

    categoryName = models.ForeignKey(itssafeCategories,
                                     on_delete=models.CASCADE,
                                     )
    categoryCode = models.CharField(max_length=20,blank=True,editable=False)

    publication_date = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='images/itssafe/',
                                  default='images/itssafe/8.png')

    audio = models.FileField(upload_to='audio/itssafe',
                             null=True)
    status = models.PositiveSmallIntegerField(default=1)


    def __unicode__(self):
        return self.titr
    def get_absolute_url(self):
        return reverse('itssafe:showpost', kwargs={'id':self.id})
    def save(self, *args, **kwargs):
        self.categoryCode='normal'+str(self.categoryName.categoryID)
        super(itssafePosts, self).save(*args, **kwargs)

    @classmethod
    def create(cls, categoryCode):
        return cls(categoryCode=categoryCode)
