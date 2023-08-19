from django.shortcuts import render
from django import forms
from django.http import Http404,HttpResponse,HttpResponseRedirect

def index(request):
    return render(request, "index.html", {
        "index": index
    })

def about(request):
    return render(request, "about.html", {
        "about": about
    })

def blog_home(request):
    return render(request, "blog-home.html", {
        "blog_home": blog_home
    })

def blog_post(request):
    return render(request, "blog-post.html", {
        "blog_post": blog_post
    })

def contact(request):
    return render(request, "contact.html", {
        "contact": contact
    })

def pricing(request):
    return render(request, "pricing.html", {
        "pricing": pricing
    })

def portfolio_overview(request):
    return render(request, "portfolio-overview.html", {
        "portfolio_overview": portfolio_overview
    })

def portfolio_item(request):
    return render(request, "portfolio-item.html", {
        "portfolio_item": portfolio_item
    })

def faq(request):
    return render(request, "faq.html", {
        "faq": faq
    })
