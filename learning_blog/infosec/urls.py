from django.contrib import admin
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('post/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('overview/', views.overview, name='overview'),
    path('item/', views.item, name='item'),
    path('faq/', views.faq, name='faq'),
]
