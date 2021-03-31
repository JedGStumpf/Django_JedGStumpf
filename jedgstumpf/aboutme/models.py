from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MyBlog(models.Model):
    title = models.CharField(max_length=79)
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.datetime)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.author} on {str(self.posted_on)}'
