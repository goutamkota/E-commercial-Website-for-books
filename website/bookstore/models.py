from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    summary = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpeg', upload_to='cover_pics')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



