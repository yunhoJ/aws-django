from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question

###### 처음코드 #######
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list,}
#     return HttpResponse(template.render(context, request))
##### 간략하게 작성 ######

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render  (request, 'polls/index.html', context)


def detail(request, question_id):
    # q=Question.objects.get(pk=question_id) 값을 못받아와 에러 발생 시킴 
    # 404페이지 띄우기
    q=get_object_or_404(Question, pk=question_id ) 
    context = {'question': q}
    return render(request,"polls/detail.html",context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)