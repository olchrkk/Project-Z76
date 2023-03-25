
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='profile')
    email = models.EmailField(unique=True)
    photo = models.ImageField(null=True, blank=True, default="default_photo_account.png")
    bio = models.TextField(null=True, blank=True)
    follows = models.ManyToManyField('UserProfile', blank=True, related_name='followers')

    def display_follows(self):
        return ", ".join([user.username for user in self.follows.all()])

    def get_user_url(self):
        return reverse('user_account', args=[self.id])


    def get_user_followers_url(self):
        return reverse('user-followers', args=[self.id])

    def get_user_following_url(self):
        return reverse('user-following', args=[self.id])

    def followsCount(self):
        return len([user for user in self.follows.all()]) if [user for user in self.follows.all()] else 0

    def followersCount(self):
        return len([user for user in self.followers.all()]) if [user for user in self.followers.all()] else 0

    def __str__(self):
        return self.user.username
