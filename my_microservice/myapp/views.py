from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def health_check(request):
    return HttpResponse("hello myapp", status=200)