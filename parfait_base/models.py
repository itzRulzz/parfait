from django.db import models

class Query(models.Model):
    text = models.TextField(default="")
    