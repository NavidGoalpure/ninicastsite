# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import ping_google
from PIL import Image
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

    thumbUrl = models.CharField(max_length=100,blank=True)

    audio = models.FileField(upload_to='audio/itssafe',
                             null=True, blank=True)
    status = models.PositiveSmallIntegerField(default=1)


    def __unicode__(self):
        return self.titr
    def get_absolute_url(self):
        return reverse('itssafe:showpost', kwargs={'id':self.id})
    def save(self, *args, **kwargs):
        self.categoryCode='safe'+str(self.categoryName.categoryID)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

        # ******create thumbnail image
        basewidth = 300
        img = Image.open(self.image)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        imgname = self.image.url
        tempChar = imgname[:1]
        imgname = imgname[1:]

        imgname = imgname.replace("/", "/thumb/images/itssafe/")
        imgname = str(imgname)
        if (tempChar != "/"):
            fullfile = tempChar + imgname
            self.thumbUrl = str(fullfile)
        else:
            fullfile = imgname
            fullfile = str(fullfile)
            self.thumbUrl = str(tempChar + fullfile)

        img.save(fullfile)
        super(itssafePosts, self).save(*args, **kwargs)

    @classmethod
    def create(cls, categoryCode):
        return cls(categoryCode=categoryCode)

