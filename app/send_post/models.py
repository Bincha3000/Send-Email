from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE
                               )
    title = models.CharField(max_length=100)
    text = models.TextField()
    writing_date = models.DateTimeField(default=timezone.now)
    sending_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField()

    def sending(self):
        self.sending_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
