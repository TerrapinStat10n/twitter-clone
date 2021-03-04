from django.db import models

# Create your models here.


class TwitterDjango(models.Model):
    id = models.AutoField(primary_key=True)
    parent_tweet_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=280)
    image_path = models.FileField('post/static/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#    def fetchForm():
#        name = request.POST.get("name")
#        text = request.POST.get("text")
#        image_path = request.POST.get("photo")
#        created_at = datetime.datetime.now()

#        post = TwitterDjango(name=name, text=text, image_path=image_path, created_at=created_at)
#        post.save()
