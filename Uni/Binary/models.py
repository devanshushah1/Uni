from django.db import models

# Create your models here.


class GitQuery(models.Model):
    username = models.CharField(max_length=200)
    repo_count = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.username
