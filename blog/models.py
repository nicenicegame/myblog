from django.db import models


# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=250)
    created_at = models.DateTimeField('created at')

    def __str__(self):
        return self.post_title
