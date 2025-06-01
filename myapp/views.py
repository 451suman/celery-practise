from django.shortcuts import render
from myapp.tasks import add, sub


def index(request):
    add.delay(1, 2)
    sub.delay(1, 2)
    return render(request, "myapp/home.html")


# def index(request):
#     # Use apply_async to call Celery tasks
#     add.apply_async(args=[1, 2])
#     sub.apply_async(args=[1, 2])

#     return render(request, "myapp/home.html")


# def index(request):


#     return render(request, "myapp/home.html")
