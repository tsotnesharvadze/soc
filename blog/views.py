from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:6]
	context={'latest_question_list':latest_question_list}
	return render(request,'blog/index.html',context)

def detail(request,question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("კითხვა არ არსებობს")
	return render(request,'blog/detail.html',{'question':question})

def results(request,question_id):
	response="შენ უყურებ რეზულტატს შეკითხვისა %s"
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("შენ ხმას აძლევ კითხვას %s"%question_id)