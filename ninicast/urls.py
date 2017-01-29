"""ninicast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from . import views
from views import PostSitemap

sitemaps = {
        'post': PostSitemap
}

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^itsnormal/', include('itsnormal.urls', namespace='itsnormal')),
                  url(r'^itssafe/', include('itssafe.urls', namespace='itssafe')),
                  url(r'^$',views.hello , name = 'mainpage'),
                  url(r'^googleab93e03628178ac3\.html$',views.googleWebmasterToolLink , name = 'mainpage'),

                  url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                  name='django.contrib.sitemaps.views.sitemap')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
