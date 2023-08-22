from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username} {self.password} {self.email}"
    
    # fullname = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    # contact = models.TextField()

    
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
  
