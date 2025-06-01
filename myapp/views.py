from django.shortcuts import render
from myapp.tasks import add, sub
from celery.result import AsyncResult

# def index(request):
#     add.delay(1, 2)
#     sub.delay(1, 2)
#     return render(request, "myapp/home.html")


# def index(request):
#     # Use apply_async to call Celery tasks
#     add.apply_async(args=[1, 2])
#     sub.apply_async(args=[1, 2])

#     return render(request, "myapp/home.html")


def index(request):
    result = add.delay(1, 2)
    return render(request, "myapp/home.html", {"result": result})


def check_result(request, task_id):
    # retrieve the task result using the task_id

    result = add.AsyncResult(task_id)
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())
    # print ("GEt: ", result.get() )
    # .get is used to retrieve the result of the task
    # If the task is not ready, it will block until the result is available
    return render(request, "myapp/result.html", {"result": result})
