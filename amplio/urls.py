from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forms/', views.forms, name='mainform'),
    # path('forms/webinar/', views.webinar, name='webinar_form'),
    path('forms/waitlist/', views.waitlist, name='waitlist_form'),
    path('admin/', admin.site.urls),
]

handler404 = 'amplio.views.handler404'
handler500 = 'amplio.views.handler500'

