from django.db import models
import uuid
# Create your models here.
class fields(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    Link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    Total_vote = models.IntegerField(default=0, null=True,blank=True)
    Vote_Ratio = models.IntegerField(default=0, null=True,blank=True)
    Date_created = models.DateField(auto_now_add=True)
    #Date_created_Modified = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title
    
class Check(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    #owner_user  = 
    # userproject = models.ForeignKey(fields,on_delete= models.SET_NULL) #fOR leave data of the user i.e means comments
    userproject = models.ForeignKey(fields,on_delete= models.CASCADE) #user data is deleted when project is deleted  
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE) 
    Date_created = models.DateField(auto_now_add=True)
    #Date_created_Modified = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    Date_created = models.DateField(auto_now_add=True)
    #Date_created_Modified = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return self.name