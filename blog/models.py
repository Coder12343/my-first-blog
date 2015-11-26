from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey('auth.User')
    create_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

