from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import User, Questions, Scores

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


'''
Users -> ( login.html | logout.html | profile.html | register.html )
'''


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
    return render(request, "home/register.html", {'form': form})


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
                # messages.success(request, f'Logged In as Instructor')
                print("Logged in as Instructor")
                return render(request, "home/instructor.html")
            else:
                print("Logged in as student")
                messages.success(request, f'Logged In as Student')
                return render(request, "home/student.html")
        else:
            print("No User found")
            messages.success(request, f'Wrong credentials (or) User not found')
            return render(request, "home/login.html", {'error': 1})
    else:
        print("Not a request POST")
        return render(request, "home/login.html")


def logout(request):
    try:
        del request.session['user']
        del request.session['email']
        del request.session['type']
        del request.session['points']
        return render(request, "home/logout.html")
    except Exception as e:
        raise e


def profile(request):
    if 'user' in request.session:
        return render(request, "home/profile.html")
    else:
        messages.success(request, f'Access Denied !!')
        return render(request, "home/home.html")


"""
Instructor level access
"""

quizzes = [
    {
        "title": "Welcome Instructor",
        "author": "Instructor",
        "content": "Create Quiz",
        "date_posted": "30-AUG-2019"
    }
]


def instructor(request):
    context = {
        "posts": quizzes
    }
    print("instructor method invoked")
    if 'user' in request.session:
        if request.session['type'] == 'instructor':
            print("Instructor Authenticated :)")
            return render(request, "home/instructor.html", context)
        else:
            messages.success(request, f'Access Denied !! ')
            return render(request, "home/home.html")
    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/login.html")


def create_quiz(request):
    if 'user' in request.session:
        if request.session['type'] == "instructor":
            print("Instructor Authenticated to create Quiz :)")

            if request.method == 'POST':
                ques = request.POST['ques']
                qtype = request.POST['qtype']
                qtype = int(qtype)
                if qtype == 1:
                    print("tf called")
                    tf_ans = request.POST['tf_ans']
                    auth = Questions(quiz_id=request.session['user'], question=ques, question_type=1, ans=tf_ans,
                                     weightage=10)
                    auth.save()
                    print("TRUE/FALSE Question submitted successfully !!")
                elif qtype == 2:
                    op1 = request.POST['opt1']
                    op2 = request.POST['opt2']
                    op3 = request.POST['opt3']
                    op4 = request.POST['opt4']
                    ans = request.POST['ans']
                    auth = Questions(quiz_id=request.session['user'], question=ques, question_type=2, op1=op1, op2=op2,
                                     op3=op3,
                                     op4=op4, ans=ans, weightage=20)
                    auth.save()
                    print("MCQ Question submitted successfully !!")
                elif qtype == 3:
                    auth = Questions(quiz_id=request.session['user'], question=ques, question_type=3, weightage=30)
                    auth.save()
                    print("ESSAY Question submitted successfully !!")

                messages.success(request, f'Question Added !!')
                return render(request, "home/create_quiz.html")

            else:
                print("Not a request POST")
                return render(request, "home/create_quiz.html")

        else:
            messages.success(request, f'Access Denied !! ')
            return render(request, "home/home.html")
    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/login.html")


def display_questions(request):
    if 'user' in request.session:
        if request.session['type'] == "instructor":
            if request.method == 'POST':
                print("Deletion requested !!")
                selection = request.POST.getlist('sel')
                user = request.session['user']
                for l in selection:
                    Questions.objects.filter(quiz_id=user, question=l).delete()
                print("Deletion Complete :)")
                que_cat1 = Questions.objects.all()
            else:
                que_cat1 = Questions.objects.all()
            context = {
                "Questions": que_cat1
            }
            return render(request, "home/display_questions.html", context)
        else:
            messages.success(request, f'Access Denied !! ')
            return render(request, "home/home.html")
    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/login.html")


def view_scores(request):
    if 'user' in request.session:
        if request.session['type'] == "instructor":

            results = Scores.objects.all()
            context = {
                "Scores": results
            }
            return render(request, "home/view_scores.html", context)
        else:
            messages.success(request, f'Access Denied !! ')
            return render(request, "home/home.html")
    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/login.html")


"""
Student Level Access
"""


def student(request):
    if 'user' in request.session:
        if request.session['type'] == "student":
            print("Student Authenticated :)")
            return render(request, "home/student.html")
        else:
            messages.success(request, f'Login as Student to view page !! ')
            return render(request, "home/instructor.html")
    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/home.html")


ref = []


def start_quiz(request):
    if 'user' in request.session:
        if request.method == 'POST':
            print("Quiz Complete !")
            score = 0
            l = [request.POST['1'], request.POST['2'], request.POST['3'], request.POST['4'],
                 request.POST['5']]

            for i, question in enumerate(ref):
                get = Questions.objects.filter(question=question)
                qtype = get[0].question_type
                actual_ans = get[0].ans
                user_ans = l[i]
                if qtype == 1 and user_ans == actual_ans:
                    score += 10
                elif qtype == 2 and user_ans == actual_ans:
                    score += 20
                elif qtype == 3:
                    if len(user_ans) > 50:
                        score += 30

            auth = Scores(user_name=request.session['user'], score=score)
            auth.save()
            current = User.objects.only('user_points').get(user_name=request.session['user']).user_points + score
            u = User.objects.filter(user_name=request.session['user']).update(user_points=current)
            messages.success(request, f'Trivia Complete ! Click view scores to see results')
            return render(request, "home/student.html")

        else:
            ques = Questions.objects.all().order_by('?')[:5]
            ref.clear()
            for j in ques:
                ref.append(j.question)
            context = {
                "Questions": ques
            }
            return render(request, "home/start_quiz.html", context)


    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/home.html")


def user_scores(request):
    if 'user' in request.session:
        if request.session['type'] == "student":
            print("Student Authenticated to view scores :)")
            user = request.session['user']
            results = Scores.objects.filter(user_name=user)
            context = {
                "Scores": results
            }
            return render(request, "home/user_scores.html", context)
        else:
            messages.success(request, f'Login as student to view page !! ')
            return render(request, "home/instructor.html")
    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/home.html")
