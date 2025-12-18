from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title   = models.CharField(
        max_length=200
    )
    post_image   = CloudinaryField('image', blank=True, null=True)
    desc    = models.TextField(
        blank=True
    )
    created_at    = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"POST({self.user},{self.title})"