from django.shortcuts import render
from django.http import HttpResponse

def Hello(request):
  return HttpResponse("Hello")
def Index(request):
  """return HttpResponse("Hello")"""
  return render(request,'Index.html')
