from datetime import date, timedelta

from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    title = models.CharField(null=True, blank=True)
    author = models.CharField(null=True, blank=True)
    publisher = models.CharField(null=True, blank=True)
    rating = models.CharField(null=True, blank=True)
    category = models.CharField(null=True, blank=True)
    image = models.CharField(null=True, blank=True)

    #@property
    #def loans(self):
        #instance = self
        #qs = Loans.objects.filter(book=instance)
        #return qs

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


#class Loans(models.Model):
    #book = models.ForeignKey(Books, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #loan_date = models.DateField(auto_now_add=date.today(), blank=False)
    #return_date = models.DateField(default=date.today()+timedelta(days=14))

    #@property
    #def username(self):
        #return self.user.username
