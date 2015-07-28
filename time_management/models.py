from django.db import models
from pooopers.models import Poooper
from datetime import datetime


class Pooop(models.Model):
    poooper = models.ForeignKey(Poooper, related_name='pooops', on_delete=models.CASCADE)
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(blank=True,null=True)

    class Meta:
        ordering = ['end']


    def duration(self):
        if self.end:
            return self.end - self.start
        else:
            return datetime.now() - self.start
