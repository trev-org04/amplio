from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticSitemap

sitemaps = {
    'static': StaticSitemap
}


urlpatterns = [
    path('', views.home, name='home'),
    path('forms/', views.forms, name='mainform'),
    path('forms/webinar/', views.webinar, name='webinar_form'),
    path('forms/waitlist/', views.waitlist, name='waitlist_form'),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = 'amplio.views.handler404'
handler500 = 'amplio.views.handler500'

