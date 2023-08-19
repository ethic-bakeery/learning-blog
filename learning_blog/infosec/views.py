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

def blog(request):
    return render(request, "blog.html", {
        "blog": blog
    })

def post(request):
    return render(request, "post.html", {
        "blog_post": post
    })

def contact(request):
    return render(request, "contact.html", {
        "contact": contact
    })

def pricing(request):
    return render(request, "pricing.html", {
        "pricing": pricing
    })

def overview(request):
    return render(request, "overview.html", {
        "overview": overview
    })

def item(request):
    return render(request, "item.html", {
        "item": item
    })

def faq(request):
    return render(request, "faq.html", {
        "faq": faq
    })
