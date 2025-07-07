import json
from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule


# if you name task you will see task name in the celery task resuld dash board
@shared_task(name="addition_task")
def add(x, y):
    sleep(20)
    print(f"Adding: {x} + {y} = {x + y}")
    return x + y


@shared_task(name="sub_task")
def sub(x, y):
    sleep(5)
    print(f"Subtracting: {x} - {y} = {x - y}")
    return x - y


@shared_task
def clear_session_cache(id):
    print(f"session cache cleared: {id}")
    return id


@shared_task
def clear_redis_data(key):
    print(f"redis data cleared: {key}")
    return key


@shared_task
def cleared_rabbitmq_data(key):
    print(f"rabbitmq data cleared: {key}")
    return key


# # if you want o create predioc task in code
# # create schedule every 20 second
# schedule, create = IntervalSchedule.objects.get_or_create(
#     every=1, period=IntervalSchedule.SECONDS
# )


# #  schedule the periodic task programmatically
# PeriodicTask.objects.get_or_create(
#     name="Clear Rabbirtmq data",
#     task="myapp.tasks.cleared_rabbitmq_data",
#     interval=schedule,
#     args=json.dumps(("123",)),
# )


def create_periodic_tasks():
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=1, period=IntervalSchedule.SECONDS
    )

    PeriodicTask.objects.get_or_create(
        name="Clear Rabbitmq data",
        task="myapp.tasks.cleared_rabbitmq_data",
        interval=schedule,
        defaults={
            "args": json.dumps(["123"]),
        },
    )
