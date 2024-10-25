from django.shortcuts import render
from myapp.tasks import add, sub  
from celery.result import AsyncResult

# Create your views here.
def index(request):
    result = add.delay(6,5)
    result1 = sub.delay(9,3)
    return render(request, 'home.html', context={"result":result, "result1":result1})

def check_result(request, task_id):
    result  = AsyncResult(id=task_id)
    return render(request, 'result_page.html', context={"result":result})