from django.db import models
from pooopers.models import Poooper
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver



class Pooop(models.Model):
    poooper = models.ForeignKey(Poooper, related_name='pooops', on_delete=models.CASCADE)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(blank=True,null=True)

    class Meta:
        ordering = ['end']


    def duration(self):
        end = self.end or timezone.now()
        dur = end - self.start
        return dur.total_seconds()
        
    def money(self):
        return self.duration() * self.poooper.salary_second()

@receiver(pre_save)
def clean_incompletes(sender,instance):
    instance.poooper.pooops.filter(end__isnull=True).delete()
        