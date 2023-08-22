from django import forms
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect, reverse,redirect

def index(request):
    if not request.user.is_authenticated:
         return HttpResponseRedirect(reverse('login'))
    return render(request, "userdetails.html")

def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "login.html", {
                "message": "try again!"
            })
    return render(request, "login.html")

    # return render(request, "login.html",{
    #     "login":login
    # })

# def user_logout(request):
#     logout(request)
#     return redirect('login')

# def user_register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

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
