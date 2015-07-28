from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin,UserManager
from datetime import timedelta
from decimal import Decimal,getcontext


class Poooper(AbstractBaseUser,PermissionsMixin):

    username                      = models.CharField(primary_key=True,max_length=40, unique=True,db_index=True)
    email                         = models.EmailField(max_length=254, unique=True)
    date_joined                   = models.DateTimeField(auto_now_add=True, blank=True)
    is_active                     = models.BooleanField(default=True)
    is_admin                      = models.BooleanField(default=False)
    is_staff                      = models.BooleanField(default=False)
    objects                       = UserManager()
    salary                        = models.DecimalField(max_digits=24, decimal_places=2,default=0)  # lo que gano en una hora
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
        "Total seconds pooping"
        total  = timedelta()
        for pooop in self.pooops.all():
            total += pooop.end - pooop.start
        return total

    def total_earned(self):
        "Total money gained pooping"
        total_poooped = self.total_poooped()
        result_float = float(self.salary) * (total_poooped.total_seconds() / 3600)
        return Decimal.from_float(result_float).quantize(Decimal('1.00'))


