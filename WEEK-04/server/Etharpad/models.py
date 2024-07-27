from django.db import models

class EtharpadClass(models.Model):
    api_key = models.CharField(max_length=200)
