from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    publised_date = models.DateField(blank=True, null=True)

    def publised(self):
        self.publised_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title    