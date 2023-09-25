from django.shortcuts import render
from django.http import HttpResponse


#def projects(request):
def projects(request):
    return HttpResponse('Here is Our Products')

#def project(request):
def project(request, pk):
    return HttpResponse('Here is Our rows and colmn' +  ' '  + str(pk))

# Create your views here.
