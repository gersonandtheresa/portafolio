from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    pic = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
