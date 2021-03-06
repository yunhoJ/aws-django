from django.urls import path
from polls import views

#url의 이름 공간 정하기  비슷한 이름으로 묶음 
app_name='polls'

urlpatterns=[
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/ 인자가 views로 들어감
    path('<int:question_id>/', views.detail, name='detail'),
  
    path('<int:question_id>/results/', views.results, name='results'),
    
    path('<int:question_id>/vote/', views.vote, name='vote'),
]  