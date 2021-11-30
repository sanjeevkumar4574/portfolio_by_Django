
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index, name='index'),
    path('about',about,name='about'),
    path('portfolio',Portfolio, name="portfolio"),
    path('blog',blog,name='blog'),
    path('contact',contact, name='contact')

]+static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)