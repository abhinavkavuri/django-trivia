from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            usertype = form.cleaned_data.get('usertype')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password1 == password2:
                user = User(user_name=username, user_password=password1, user_type=usertype, user_email=email,
                            user_points=30)
                user.save()
                print("New User Registered.")
                messages.success(request, f'Account created for {username}!')
                return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form': form})


def login_view(request):
    if request.method == 'POST':

        user_name = request.POST['uname']
        password = request.POST['pass']
        retr = User.objects.filter(user_name=user_name, user_password=password)
        if retr:
            print("user found !!")
            email = User.objects.only('user_email').get(user_name=user_name, user_password=password).user_email
            points = User.objects.only('user_points').get(user_name=user_name, user_password=password).user_points
            utype = User.objects.only('user_type').get(user_name=user_name, user_password=password).user_type
            print(utype)
            request.session['user'] = user_name
            request.session['email'] = email
            request.session['type'] = utype
            request.session['points'] = points
            print("SESSION INVOKED -->Name  = " + request.session['user'] + " Logged in.")
            if utype == "instructor":
                #messages.success(request, f'Logged In as Instructor')
                print("Logged in as Instructor")
                return render(request, "instructor/instructor.html")
            else:
                print("Logged in as student")
                messages.success(request, f'Logged In as Student')
                return render(request, "student/student.html")
        else:
            print("No User found")
            messages.success(request, f'Wrong credentials (or) User not found')
            return render(request, "users/login.html", {'error': 1})
    else:
        print("Not a request POST")
        return render(request, "users/login.html")


def logout(request):
    try:
        del request.session['user']
        del request.session['email']
        del request.session['type']
        del request.session['points']
        return render(request, "users/logout.html")
    except Exception as e:
        raise e


def profile(request):
    if 'user' in request.session:
        return render(request, "users/profile.html")
    else:
        messages.success(request, f'Access Denied !!')
        return render(request, "home/home.html")
