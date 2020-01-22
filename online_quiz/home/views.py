from django.shortcuts import render
from django.http import HttpResponse

import home
from django.contrib.auth import authenticate, login, logout

'''
Home -> templates -> home -> ( base.html | home.html | about.html )
'''

posts = [
    {
        "title": "Welcome to Trivia Quiz",
        "author": "Lorem Ipsum",
        "content": "Start by clicking Login",
        "date_posted": "27-AUG-2019"
    },
    {
        "title": "Want to post questions ?",
        "author": "Jane Doe",
        "content": "Login as Instructor",
        "date_posted": "28-AUG-2019"
    }

]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "home/home.html", context)


def about(request):
    return render(request, "home/about.html", {"title": "About us !!"})


def register_page(request):
    return render(request, "home/register_page.html")


def login_redirect(request):
    return render(request, "home/login.html")


def login(request):
    if request.method == 'POST':
        user_name = request.POST['uname']
        password = request.POST['pass']
        # print(user_name)
        if User.objects.filter(user_name=user_name, user_password=password):
            print(User.objects.get(user_name=user_name, user_password=password))
            # str,x=User.objects.get(user_name =user_name,user_password = password)
            # print(x)
            points = User.objects.only('user_points').get(user_name=user_name, user_password=password).user_points
            utype = User.objects.only('user_type').get(user_name=user_name, user_password=password).user_type
            USER = User.objects.all()
            print(utype)
            print("ONE TUPLE")
            request.session['user'] = user_name
            print("SESSION INVOKED -->Name  = " + request.session['user'] + " Logged in.")
            if utype == "Quiz-Master":
                return render(request, "quiz_master/master_profile.html", {"Data": points})
            else:
                return render(request, "Player/profile.html", {"Data": points})
        else:
            print("NO TUPLES")
            return render(request, "home/login.html", {'error': 1})


def logout(request):
    try:
        del request.session['user']
        print("User Logged out.")
        return render(request, "Reg/logout.html")
    except Exception as e:
        raise e
