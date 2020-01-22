from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView
from .models import Questions
from student.models import Scores

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
        if request.session['user'] == 'instructor':
            print("Instructor Authenticated :)")
            return render(request, "instructor/instructor.html", context)
        else:
            messages.success(request, f'Access Denied !! ')
            return render(request, "home/home.html")
    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/home.html")


def create_quiz(request):
    if request.method == 'POST':
        ques = request.POST['ques']
        qtype = request.POST['qtype']
        qtype = int(qtype)
        if qtype == 1:
            print("tf called")
            tf_ans = request.POST['tf_ans']
            auth = Questions(quiz_id=request.session['user'], question=ques, question_type=1, ans=tf_ans, weightage=10)
            auth.save()
            print("TRUE/FALSE Question submitted successfully !!")
        elif qtype == 2:
            op1 = request.POST['opt1']
            op2 = request.POST['opt2']
            op3 = request.POST['opt3']
            op4 = request.POST['opt4']
            ans = request.POST['ans']
            auth = Questions(quiz_id=request.session['user'], question=ques, question_type=2, op1=op1, op2=op2, op3=op3,
                             op4=op4, ans=ans, weightage=20)
            auth.save()
            print("MCQ Question submitted successfully !!")
        elif qtype == 3:
            auth = Questions(quiz_id=request.session['user'], question=ques, question_type=3, weightage=30)
            auth.save()
            print("ESSAY Question submitted successfully !!")

        messages.success(request, f'Question Added !!')
        return render(request, "instructor/create_quiz.html")

    else:
        print("Not a request POST")
        return render(request, "instructor/create_quiz.html")



def display_questions(request):
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
    return render(request, "instructor/display_questions.html", context)


def view_scores(request):

    results = Scores.objects.all()
    context = {
        "Scores": results
    }
    return render(request, "instructor/view_scores.html", context)
