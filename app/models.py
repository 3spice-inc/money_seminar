from django.db import models
from mdeditor.fields import MDTextField
# Create your models here.



class Article(models.Model):
    title=models.CharField(max_length=100)
    content =MDTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title