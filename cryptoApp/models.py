from django.db import models

# Create your models here.
class ItemRegist(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class ContentTable(models.Model):
    heading = models.CharField(max_length=255)
    listItems = models.CharField(max_length=2500)


class blogTable(models.Model):
    blogHeading = models.CharField(max_length=255)
    blogAuthor = models.CharField(max_length=255)
    summaryDesc = models.CharField(max_length=255)
    imgDesc = models.CharField(max_length=255,default='null')

