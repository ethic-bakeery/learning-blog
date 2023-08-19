from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('blog_home.html/', views.blog_home, name='blog_home'),
    path('blog_post.html/', views.blog_post, name='blog_post'),
    path('contact.html/', views.contact, name='contact'),
    path('pricing.html/', views.pricing, name='pricing'),
    path('portfolio_overview.html/', views.portfolio_overview, name='portfolio_overview'),
    path('portfolio_item.html/', views.portfolio_item, name='portfolio_item'),
    path('faq.html/', views.faq, name='faq'),
]
