from django.contrib import admin

# Register your models here.
from .models import fields,Check,Tag

admin.site.register(fields)
admin.site.register(Check)
admin.site.register(Tag)