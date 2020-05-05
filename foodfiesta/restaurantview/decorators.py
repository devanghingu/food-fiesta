from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models     import Group

def check_is_restaurant(func):

    def check_is_user_group(user):
        ''' Check User in which Group Wrapper function'''
        return user.groups.filter(name='staff_group').exists()
        
    pass_test = user_passes_test(check_is_user_group)
    return pass_test(func)

