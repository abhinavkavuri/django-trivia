from django.contrib import messages
from django.shortcuts import render
from .models import Scores
from instructor.models import Questions
from users.models import User

def student(request):
    if 'user' in request.session:
        print("Student Authenticated :)")
        return render(request, "student/student.html")
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
            messages.success(request,f'Trivia Complete ! Click view scores to see results')
            return render(request, "student/student.html")

        else:
            ques = Questions.objects.all().order_by('?')[:5]
            ref.clear()
            for j in ques:
                ref.append(j.question)
            context = {
                "Questions": ques
            }
            return render(request, "student/start_quiz.html", context)


    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/home.html")


def user_scores(request):
    if 'user' in request.session:
        print("Student Authenticated to view scores :)")
        user = request.session['user']
        results = Scores.objects.filter(user_name=user)
        context = {
            "Scores": results
        }
        return render(request, "student/user_scores.html", context)
    else:
        messages.success(request, f'Login to view page !! ')
        return render(request, "home/home.html")
