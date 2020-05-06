from django.db import models
from django.contrib.auth.models import AbstractUser
from adminview.models import City

class User(AbstractUser):
    profile=models.ImageField(upload_to='profile/',blank=True,null=True)

    def __str__(self):
        return self.username

#User
class Address(models.Model):
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(max_length=255)
    default = models.BooleanField(default=False)
    city    = models.ForeignKey(City,on_delete=models.CASCADE)
    contact = models.CharField(max_length=13)

    def __str__(self):
        return self.user.username

    

