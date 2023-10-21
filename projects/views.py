# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

FuseItemsList = [

{
'id':'1',
'title':'Economic Website',
'description':'Fully Function Economic Website'
},
{
'id':'2',
'title':'School Website',
'description':'A Website for school for demo purpose'
},
{
'id':'3',
'title':'Productio Website',
'description':'Production website after dev and staging server'
},

]


#def projects(request):
def projects(request):
    msg = 'Hello You are on the Projects Page ' # msg discribe 1
    page = 'projects-1'
    number= 10 # Varaible declartion for condn and apply logic in template projects-1.html
    context = {'message':msg,'page':page,'number':number,'ItemList':FuseItemsList} #dynamic Content
    #return HttpResponse('Here is Our Products')  #Simple Http Response
        # return render(request, 'fuse/projects-1.html',{'message':msg,'page':page}) # use render func to call templates, use msg discribe 2 in dictionary format Nme:Key
    return render(request, 'fuse/projects-1.html', context ) # use render func to call templates, use msg discribe 2 in dictionary format Nme:Key


#def project(request):

def project(request, pk):
    ItemObj = None
    for i in FuseItemsList:
        if i['id'] == pk:
            ItemObj = i
    #return HttpResponse('Here is Our rows and colmn' +  ' '  + str(pk)) #Simple Http Response
    return render(request, 'fuse/simple-projects-1.html',{'items1':ItemObj}) # use render func to call templates ,we are in root folder and use fuse for templates



