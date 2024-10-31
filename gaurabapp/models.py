from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class SaveDetail(models.Model):
    username = models.CharField(max_length=150, blank=False, null=False,)
    password = models.CharField(max_length=128, blank=False,null=False)  


    def __str__(self):
        return self.username
