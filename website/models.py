from django.db import models

# Create your models here.
# here are defining class 
# no matter what database are you using this model file always be the same 
class Record(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True)
    # any time a model created this will add a timestamp on them 
    # this is database model 
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    address = models.CharField(max_length=55) 
    city =  models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    zipcode = models.CharField(max_length=55)
    # what this function mean ???
    def __str__(self):
        return (f"{self.first_name} {self.last_name}" )