from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin,UserManager


class Poooper(AbstractBaseUser,PermissionsMixin):

    username                      = models.CharField(primary_key=True,max_length=40, unique=True,db_index=True)
    email                         = models.EmailField(max_length=254, unique=True)
    date_joined                   = models.DateTimeField(auto_now_add=True, blank=True)
    is_active                     = models.BooleanField(default=True)
    is_admin                      = models.BooleanField(default=False)
    is_staff                      = models.BooleanField(default=False)
    objects                       = UserManager()    
    full_name                     = models.CharField(max_length=254,blank=True,null=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        return u'%s' % (self.username)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.username

    def total_poooped(self):
        pass