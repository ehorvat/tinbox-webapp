"""website URL Configuration

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
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', include('tinbox.urls', namespace="tinbox")),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/register/', 'accounts.views.register', name="registration_register"),
    url(r'^dashboard/', 'accounts.views.dashboard', name="dashboard"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^product/', include('catalog.urls', namespace="product")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shopping/', include('shopping.urls')),
    url(r'^payments/', include("payments.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
