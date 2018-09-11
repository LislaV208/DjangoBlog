from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # default='default.png', 
    thumb = models.ImageField(blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        initLength = len(self.body)
        newLength = 160
        result = self.body[:newLength]

        if initLength > newLength:
            result += '...'

        return result