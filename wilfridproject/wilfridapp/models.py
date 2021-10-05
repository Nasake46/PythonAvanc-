from django.db import models

class Website ( models.Model):
    host = models.CharField(max_length=512)
    is_up = models.BooleanField()
    last_check = models.DateTimeField(auto_now=True)
