from django.contrib import admin
from .models import Follower, User,Post,Following,Like,Profile_Picture

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Follower)
admin.site.register(Following)
admin.site.register(Like)
admin.site.register(Profile_Picture)