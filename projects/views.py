# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import fields
from .forms import ProjForm

# FuseItemsList = [

# {
# 'id':'1',
# 'title':'Economic Website',
# 'description':'Fully Function Economic Website'
# },
# {
# 'id':'2',
# 'title':'School Website',
# 'description':'A Website for school for demo purpose'
# },
# {
# 'id':'3',
# 'title':'Productio Website',
# 'description':'Production website after dev and staging server'
# },

# ]


#def projects(request):
def projects(request):
    projects1 = fields.objects.all() # Queries of database 
    context = {'ItemList': projects1 } #dynamic Content and import data from database with project name 
    #return HttpResponse('Here is Our Products')  #Simple Http Response
        # return render(request, 'fuse/projects-1.html',{'message':msg,'page':page}) # use render func to call templates, use msg discribe 2 in dictionary format Nme:Key
    return render(request, 'fuse/projects-1.html', context ) # use render func to call templates, use msg discribe 2 in dictionary format Nme:Key


#def project(request):

def project(request, pk):
    ItemObj = fields.objects.get(id=pk)
    # tags = ItemObj.tags.all()
    #return HttpResponse('Here is Our rows and colmn' +  ' '  + str(pk)) #Simple Http Response
    return render(request, 'fuse/simple-projects-1.html',{'items1':ItemObj}) # use render func to call templates ,we are in root folder and use fuse for templates

def CreateProject(request):  
    form = ProjForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('projects')

    context = {'form' : form}
    return render(request,"fuse/projects_crup.html",context)

def UpdateProject(request,pk):  
    project = fields.objects.get(id=pk)
    form = ProjForm(instance=project)

    if request.method == 'POST':
        form = ProjForm(request.POST,instance=project)
        form.save()
        return redirect('projects')

    context = {'form' : form}
    return render(request,"fuse/projects_crup.html",context)


def deleteProject(request,pk):
    project = fields.objects.get(id=pk)
    context = {'object' : project }
    return  render(request, "fuse/delete_Object.html" , context)