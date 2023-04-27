from django.contrib import admin
from .models import Record
# Register your models here.
# here we can post the models to the admin page
# those fields we have created to the model field 
admin.site.register(Record)