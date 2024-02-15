from django.forms import ModelForm
from .models import fields

class ProjForm(ModelForm):
    class Meta: #meta is class which fetch to models class field
        model = fields
        fields = ['title','description','Link','source_link','tags']
        # fields = '__all__'
