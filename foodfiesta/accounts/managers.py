from django.db import models
# from accounts.models import User
# from django.contrib.auth import get_user_model
# User=get_user_model()
# from django.contrib.auth.models import User 

class AddressManager(models.Manager):
    def get_user_address(self,user_id):
        # user    =   User.objects.get(id=3)
        return self.filter(user__id=user_id,default=True).first()