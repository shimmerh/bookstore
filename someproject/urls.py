"""someproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from myapp.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', MyView.as_view()),
	url(r'^test/$', test),
	url(r'^publishers/$', PublisherList.as_view()),
	url(r'^publishers/(?P<pk>[0-9]+)/$', PublisherDetail.as_view()),
	url(r'^authors/$', AuthorList.as_view(),name='author-list'),
	url(r'^author/(?P<pk>[0-9]+)/$', AuthorDetail.as_view(), name='author-detail'),
	url(r'^author/add/$', AuthorCreate.as_view()),
	url(r'^author/(?P<pk>[0-9]+)/update/$', AuthorUpdate.as_view(),name='author-update'),
	url(r'^author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(),name='author-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
