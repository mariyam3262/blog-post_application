from django.db import models
from user.models import CustomUser

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.TextField("Enter post", max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "post"