from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question, Choice

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
    # 데이터 베이스 저장 
    question = get_object_or_404(Question, pk=question_id) 
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])#input name값 
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # form을 통한post response는 reverse를 보통 사용함 
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))