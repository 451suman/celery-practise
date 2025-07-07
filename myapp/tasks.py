from celery import shared_task
from time import sleep


# if you name task you will see task name in the celery task resuld dash board
@shared_task(name="sumantask.add")
def add(x, y):
    sleep(20)
    print(f"Adding: {x} + {y} = {x + y}")
    return x + y


@shared_task
def sub(x, y):
    sleep(5)
    print(f"Subtracting: {x} - {y} = {x - y}")
    return x - y
    