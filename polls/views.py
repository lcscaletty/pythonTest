from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, loader
from .models import Question
from django.shortcuts import get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html",context)
def details(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id);
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
def detail(request, question_id):
    question =get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})
