from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title
