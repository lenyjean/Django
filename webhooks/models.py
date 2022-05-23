from django.db import models
from django.db.models import JSONField
# Create your models here.  

class MessengerData(models.Model):
    data = JSONField()

