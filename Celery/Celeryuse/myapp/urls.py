from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<str:task_id>', views.check_result, name='check_result')
]
