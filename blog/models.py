from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts')
    content = models.TextField(blank=True)
    cover = models.ImageField(upload_to='source/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='liked_posts')
    commented = models.ManyToManyField(User, blank=True, related_name='commented_posts')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def likesCount(self):
        return len([like for like in self.likes.all()]) if [[like for like in self.likes.all()]] else 0

    def commentsCount(self):
        return len([comment for comment in self.commented.all()]) if [[comment for comment in self.commented.all()]] else None


class Comment(models.Model):
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    likes = models.ManyToManyField(User, blank=True, related_name='liked_comments')

    def __str__(self):
        return self.content

    def likesCount(self):
        return len([like for like in self.likes.all()]) if [[like for like in self.likes.all()]] else None
