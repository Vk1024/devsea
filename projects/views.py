# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


#def projects(request):
def projects(request):
    msg = 'Hello You are on the Projects Page ' # msg discribe 1
    #return HttpResponse('Here is Our Products')  #Simple Http Response
    return render(request, 'fuse/projects-1.html',{'message':msg}) # use render func to call templates, use msg discribe 2 in dictionary format Nme:Key

#def project(request):
def project(request, pk):
    #return HttpResponse('Here is Our rows and colmn' +  ' '  + str(pk)) #Simple Http Response
    return render(request, 'fuse/simple-projects-1.html') # use render func to call templates ,we are in root folder and use fuse for templates



