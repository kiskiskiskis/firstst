from django.db import models


# Create your models here.

class Article():
    title = models.CharField()
    body = models.CharField()