from django.db import models
from django.db.models.fields.related import ForeignKey

class Website(models.Model):
    host = models.CharField(max_length=512)
    is_up = models.BooleanField()
    last_check = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.host
    

class CheckWebsite(models.Model):
    is_up = models.BooleanField()
    date = models.DateTimeField(auto_now=True)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    message = models.CharField(max_length=512)
    def __str__(self) -> str:
        if self.is_up:
            return self.website.host +"is up"
        else:
            return self.website.host +"is down"

class WebsiteListView(models.Model):
    model = Website

class WebsiteForm(models.Model):
    host = models.CharField(label='Website hostname',
                           max_length=512)
    
