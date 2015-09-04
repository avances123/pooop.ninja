from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin,UserManager
from datetime import timedelta


class Poooper(AbstractBaseUser,PermissionsMixin):

    username                      = models.CharField(primary_key=True,max_length=40, unique=True,db_index=True)
    email                         = models.EmailField(max_length=254, unique=True)
    date_joined                   = models.DateTimeField(auto_now_add=True, blank=True)
    is_active                     = models.BooleanField(default=True)
    is_admin                      = models.BooleanField(default=False)
    is_staff                      = models.BooleanField(default=False)
    objects                       = UserManager()
    salary                        = models.IntegerField(blank=True,null=True)
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
        return self.username

    def total_poooped(self):
        "Total seconds pooping"
        total  = timedelta()
        for pooop in self.pooops.all():
            if pooop.end:
                total += pooop.end - pooop.start
        return total

    def total_earned(self):
        "Total money gained pooping"
        total_poooped = self.total_poooped()
        return self.salary * (total_poooped.total_seconds() / (30 * 3600))


