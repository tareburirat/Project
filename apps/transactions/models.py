from django.db import models

# Create your models here.
class Transaction(models.Model):
    subject = models.CharField(max_length=100)
    object_trans = models.CharField(max_length=100)
    date_action = models.DateTimeField(verbose_name="Date", auto_now=True)
    action = models.CharField(verbose_name="Action",max_length=50)

