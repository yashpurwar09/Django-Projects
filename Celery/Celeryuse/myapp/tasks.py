from celery import shared_task
from time import sleep

@shared_task(name="Addition")
def add(x,y):
    sleep(20)
    return x+y

@shared_task(name="Subtraction")
def sub(x,y):
    sleep(10)
    return x-y

@shared_task(name='Scheduled Task')
def scheduled_task(id):
    sleep(20)
    return 'You are scheduled.'