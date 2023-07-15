
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app3_string(request):
    return HttpResponse('string1')
def app3_string(request):
    return render(request,app3_srting.html)