
from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path ("create_post", views.create_post, name="create_post"),
    path ("view_all_posts", views.view_all_posts, name="view_all_posts"),
    path ("user_profile", views.user_profle, name="user_profle"),
 #   path('<str:username>/', views.Profile.as_view(), name='user_profile'),
    path ("follow/", views.follow, name="follow"),
    path ("user_id/", views.get_user_id, name="user_id"),
    path("visit_user_profle/<int:userid>", views.visit_user_profle, name="visit_user_profle"),
    path ("following_page", views.followig_page, name="following_page"),
   path ("edit_post/", views.edit_post, name="edit_post"),
   path ("unfollow/", views.unfollow, name="unfollow"),
   path ("like/", views.like, name="like"),
   path ("check_like/<str:postid>/", views.like_check, name="check_like"),
   path ("unlike/", views.unlike, name="unlike"),
   path ("dislike/", views.dislike, name="like"),
   path ("check_dislike/<str:postid>/", views.dislike_check, name="check_dislike"),
   path ("undislike/", views.undislike, name="undislike")

]
