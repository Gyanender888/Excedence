from __future__ import unicode_literals

from django.db import models
import datetime


class Client(models.Model):
    Name = models.CharField(max_length=255)
    priority = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return "Name:{}|Priority:{}".format(self.Name, self.priority)

    def __str__(self):
        return "Name:{}|Priority:{}".format(self.Name, self.priority)


class FeatureRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    Associated_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Date = models.DateField(default=datetime.datetime.today)
    PA=((0,'Policies'),(1,'Billing'),(2,'Claims'),(3,'Reports'))
    Product_Area=models.PositiveIntegerField(choices=PA,blank=True,null=True)

    def __unicode__(self):
        return "title:{}|client:{}|date:{}".format(self.title, self.Associated_client, self.Date)

    def __str__(self):
        return "title:{}|client:{}|date:{}".format(self.title, self.Associated_client, self.Date)
