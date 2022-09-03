from django.http import HttpResponse


def home(request):
    return HttpResponse("Goodbuy, World! Enjoy the sail!")

