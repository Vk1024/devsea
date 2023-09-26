from django.shortcuts import render
from django.http import HttpResponse


#def projects(request):
def projects(request): 
    #return HttpResponse('Here is Our Products')  #Simple Http Response
    return render(request,'projects-1.html') # use render func to call templates

#def project(request):
def project(request, pk):
    #return HttpResponse('Here is Our rows and colmn' +  ' '  + str(pk)) #Simple Http Response
    return render(request,'simple-projects-1.html') # use render func to call templates


# Create your views here.
