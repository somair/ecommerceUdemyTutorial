"""ecommerceProject URL Configuration

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
# FOR STATIC FILES
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from Profile import views as profileViews
from Contact import views as contactViews
from checkout import views as checkoutViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profileViews.home, name='profileHome'),
    url(r'^about/$', profileViews.about, name='profileAbout'),
    url(r'^profile/$', profileViews.userProfile, name='userProfile'),
    url(r'^contact/$', contactViews.contact, name='contactContact'),
    url(r'^checkout/$', checkoutViews.checkout, name='checkout'),
    url(r'^accounts/', include('allauth.urls')), #FOR DJANGO-ALLAUTH
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)