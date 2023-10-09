from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def user(request):
    st = "<p>이름 : 조인환</p><p>별명 : 인환</p>"

    return HttpResponse(st)
