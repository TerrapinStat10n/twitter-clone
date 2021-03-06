from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class TwitterDjango(models.Model):
    id = models.AutoField(primary_key=True)
    parent_tweet_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=280)
    image_path = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
