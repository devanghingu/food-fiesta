from django.db import models
from foodfiesta.constants import OPEN


class RestaurantManager(models.Manager):
    """restaurant mananger"""

    def check_restaurent_online(self, restaurant_id):
        print(restaurant_id)
        rest_online = self.filter(id=restaurant_id, open=OPEN)
        if rest_online.exists():
            return rest_online.get()  # return restaurant information when it's aonline
        return False  # when restaurant Offline

    def get_restaurant_item(self, rest_id):
        pass


class MenuManager(models.Manager):
    def check_item_available():
        pass
