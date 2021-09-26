from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, RESTRICT
from django.utils import tree

class User(AbstractUser):
    followers  = models.IntegerField(default=0)
    followings =models.IntegerField(default=0)

    def __str__(self):
        return f" {self.username}: {self.followers}:  {self.followings}"


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_creator")

    title = models.CharField(max_length=250,default='Title')
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f" {self.user}: {self.title}: {self.date_posted}"





class Follower(models.Model):
    main_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Person")
    user_follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower")

    def __str__(self):
        return f" {self.main_user}: {self.user_follower}: {self.user_follower.id}"



class Following(models.Model):
  usermain = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="main_user")
  user_following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following")
  def __str__(self):
        return f" {self.usermain}: {self.user_following}"



class Like(models.Model):
    main_user = models.ForeignKey(    #post creator id
        User, on_delete=models.CASCADE, related_name="post_owner")
    post_like_user = models.ForeignKey(    #id of the user whi liked the post
        User, on_delete=models.CASCADE, related_name="post_like")
    post_id = models.ForeignKey(     # id of the post
        Post, on_delete=models.CASCADE, related_name="post")

    user_liked = models.BooleanField(default=False)
    user_disliked = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.id}: {self.main_user.username}: {self.post_like_user.username}"
