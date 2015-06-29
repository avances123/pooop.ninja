from django.db import models
from pooopers.models import Poooper

class Pooop(models.Model):
    poooper = models.ForeignKey(Poooper, related_name='pooops', on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()

    class Meta:
        ordering = ['end']


    def duration(self):
        return self.end - self.start
