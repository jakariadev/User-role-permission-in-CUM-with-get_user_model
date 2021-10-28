from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    pageno= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
