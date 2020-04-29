from django.db import models

class RestaurantManager(models.Manager):
    """restaurant mananger"""    
    def check_restaurent_online(self,restaurant_id):
        rest_online=self.filter(restaurant_id,open=True)
        if rest_online.exists():
            return rest_online.get() #return restaurant information when it's aonline 
        return False # when restaurant Offline
