from django.db import models

# Create your models here.

class UserInfo(models.Model):
    '''User form'''

    uname = models.CharField(max_length=20)
    userpwd = models.CharField(max_length=40)
    useremail = models.CharField(max_length=30)

    def __unicode__(self):
        return self.username
