from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator


from .models import Post, User,Follower,Following,Like

@login_required(login_url='/login')
def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



@login_required(login_url='/login')
def create_post(request):
    if request.method == "POST":
        post = request.POST["new-post"]
        if (post == ''):
            messages.error(request, 'Post is empty')
            return HttpResponseRedirect(reverse("index"))
        usr = request.user
        if (len(post)>0):
            create_post = Post.objects.create(title = post, user_id  = usr.id)
            create_post.save()
            messages.success(request, 'Your comment has been posted!')
            return HttpResponseRedirect(reverse("index"))
        
             
@login_required(login_url='/login')
def view_all_posts(request):
    usr = request.user
    all_posts  = Post.objects.all().order_by('-date_posted')

    lst =[]
    if (all_posts.count() >0):
        for i in all_posts:
           lst.append( i.id)


    if(len(lst)>0):
        for i in lst:
            post_obj =Post.objects.get(id= i)
            like_count = Like.objects.filter(post_id = post_obj.id,user_liked=True)
            dislike_count =Like.objects.filter(post_id = post_obj.id,user_disliked=True)
            Post.objects.filter(id=i).update(likes=like_count.count(),dislikes=dislike_count.count())

    all_posts  =  Post.objects.all().order_by('-date_posted')


    post_paginator = Paginator(all_posts,10)
    page_num = request.GET.get('page')
    page = post_paginator.get_page(page_num)



    return render(request, "network/view_all_posts.html",{
        "post":page
    })
   

@login_required(login_url='/login')
def user_profle(request):
    usr = request.user
    all_posts  = Post.objects.filter(user_id=usr).order_by('-date_posted')
    profile_details = User.objects.get(id=usr.id)

    lst =[]
    if (all_posts.count() >0):
        for i in all_posts:
           lst.append( i.id)


    if(len(lst)>0):
        for i in lst:
            post_obj =Post.objects.get(id= i)
            like_count = Like.objects.filter(post_id = post_obj.id,user_liked=True)
            dislike_count =Like.objects.filter(post_id = post_obj.id,user_disliked=True)
            Post.objects.filter(id=i).update(likes=like_count.count(),dislikes=dislike_count.count())

    all_posts  = Post.objects.filter(user_id=usr).order_by('-date_posted')

    mainuser = User.objects.filter(id = usr.id)
    followers_count = Follower.objects.filter(user_follower = mainuser[0])
    following_count = Follower.objects.filter(main_user = mainuser[0])



    
    post_paginator = Paginator(all_posts,10)
    page_num = request.GET.get('page')
    page = post_paginator.get_page(page_num)


    return render(request, "network/user_profile.html",{
        "all_posts":page,
        "profile_details":profile_details,
        "current_user":usr.id,
        "followers":followers_count.count(),
        "following": following_count.count()
    })

 
   
@csrf_exempt
@login_required(login_url='/login')
def get_user_id(request):
 
    usr = request.user   
    return JsonResponse(usr.id, safe=False)



@login_required(login_url='/login')
def visit_user_profle(request,userid):
   
    usr = userid
    current_user = request.user
    all_posts  = Post.objects.filter(user_id=usr).order_by('-date_posted')
    profile_details = User.objects.get(id=usr)



    lst =[]
    if (all_posts.count() >0):
        for i in all_posts:
           lst.append( i.id)


    if(len(lst)>0):
        for i in lst:
            post_obj =Post.objects.get(id= i)
            like_count = Like.objects.filter(post_id = post_obj.id,user_liked=True)
            dislike_count =Like.objects.filter(post_id = post_obj.id,user_disliked=True)
            Post.objects.filter(id=i).update(likes=like_count.count(),dislikes=dislike_count.count())

     #also need to implement it for dislikes.       

    all_posts  = Post.objects.filter(user_id=usr).order_by('-date_posted')



    followers = Follower.objects.filter(main_user=current_user.id,user_follower=usr)
    follow_ind = False

    if(len(followers)>0):
        follow_ind = True


    mainuser = User.objects.filter(id = current_user.id)
    followers_count = Follower.objects.filter(user_follower = usr)
    following_count = Follower.objects.filter(main_user = usr)

    post_paginator = Paginator(all_posts,10)
    page_num = request.GET.get('page')
    page = post_paginator.get_page(page_num)

    return render(request, "network/visit_user_profile.html",{
        "all_posts":page,
        "profile_details":profile_details,
        "current_user":current_user.id,
        "follow_ind":follow_ind,
        "followers":followers_count.count(),
        "following": following_count.count(),
        "current_user":current_user.id
    })


@csrf_exempt
def edit_post(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    post= data.get("post","")
    post_id = data.get("postid","")


    Post.objects.filter(id = post_id).update(title = post)  
    return JsonResponse({"message": "Post updated successfully!!!"}, status=201)



@csrf_exempt
@login_required(login_url='/login')
def follow(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    follower_id= data.get("follower_id","")


    mainuser = User.objects.get(id=request.user.id)
    followerid = User.objects.get(id= follower_id)

    create_follower = Follower.objects.create(main_user = mainuser, user_follower = followerid)
    create_follower.save()
   # get the follower id using java script and get the current user id from request object

    return JsonResponse({"message": "You are now folowing this user"}, status=201)



@csrf_exempt
@login_required(login_url='/login')
def unfollow(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    follower_id= data.get("follower_id","")
    mainuser = User.objects.get(id=request.user.id)
    followerid = User.objects.get(id= follower_id)

    Follower.objects.filter(main_user = mainuser, user_follower = followerid).delete()
    
   # get the follower id using java script and get the current user id from request object

    return JsonResponse({"message": "Unfollowed the user"}, status=201)



@login_required(login_url='/login')
def followig_page(request):
   
    usr = request.user.id
    following = Follower.objects.filter(main_user=usr)

    folloiwng_list =[]
    for follows in following:
        folloiwng_list.append(follows.user_follower.id)


    following_posts  = Post.objects.filter(user_id__in=folloiwng_list).order_by('-date_posted')


    lst =[]
    if (following_posts.count() >0):
        for i in following_posts:
           lst.append( i.id)


    if(len(lst)>0):
        for i in lst:
            post_obj =Post.objects.get(id= i)
            like_count = Like.objects.filter(post_id = post_obj.id,user_liked=True)
            dislike_count =Like.objects.filter(post_id = post_obj.id,user_disliked=True)
            Post.objects.filter(id=i).update(likes=like_count.count(),dislikes=dislike_count.count())


    post_paginator = Paginator(following_posts,10)
    page_num = request.GET.get('page')
    page = post_paginator.get_page(page_num)


  #  profile_details = User.objects.get(id=usr)
    return render(request, "network/following_page.html",{
        "all_posts":page
    })


@csrf_exempt
def like(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
   
    usr = request.user.id
    post_id = data.get("postid","")

    postid = Post.objects.get(id=post_id)
    liker = User.objects.get(id=usr)
    post_onwer_id = Post.objects.get(id= post_id)

    
    prev_liked = Like.objects.filter(main_user = post_onwer_id.user, post_like_user = liker,post_id = postid)
    print(prev_liked.count())

    ind = False
    if (prev_liked.count() ==0):
        ind = True
    elif(prev_liked.count() >0 and prev_liked[0].user_disliked == True):
        Like.objects.filter(main_user = post_onwer_id.user, post_like_user = liker,post_id = postid).delete()
        ind = True

   # if you want post owner not to like the his own post then turn this check on 
   # if usr == post_onwer_id.user.id:
    #    ind = False


    
    if (ind == True ):
        like_post = Like.objects.create(main_user = post_onwer_id.user, post_like_user = liker,post_id = postid,user_liked = True)
        like_post.save()
    else:
        print("already liked")
  
    return JsonResponse({"message": "Post updated successfully!!!"}, status=201)




@csrf_exempt
@login_required(login_url='/check_like')
def like_check(request,postid):
    
   # data = json.loads(request.body)
    usr = request.user.id

    postid = Post.objects.get(id=postid)
    liker = User.objects.get(id=usr)
    post_onwer_id = Post.objects.get(id= postid.id)



    prev_liked = Like.objects.filter(main_user = post_onwer_id.user, post_like_user = liker,post_id = postid,user_liked=True)

    if (prev_liked.count() ==0):  # not liked the post
        return JsonResponse(True, safe=False)
    
    return JsonResponse(False, safe=False)


@csrf_exempt
def unlike(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
   
    usr = request.user.id
    post_id = data.get("postid","")

    postid = Post.objects.get(id=post_id)
    liker = User.objects.get(id=usr)
    post_onwer_id = Post.objects.get(id= post_id)

    
    Like.objects.filter(main_user = post_onwer_id.user, post_like_user = liker,post_id = postid,user_liked=True).delete()
  
    return JsonResponse({"message": "Post updated successfully!!!"}, status=201)

@csrf_exempt
@login_required(login_url='/check_like')
def dislike_check(request,postid):
    
   # data = json.loads(request.body)
    usr = request.user.id

    postid = Post.objects.get(id=postid)
    liker = User.objects.get(id=usr)
    post_onwer_id = Post.objects.get(id= postid.id)



    prev_liked = Like.objects.filter(main_user = post_onwer_id.user, post_like_user = liker,post_id = postid,user_liked=False)

    if (prev_liked.count() ==0):  # not liked the post
        return JsonResponse(True, safe=False)
    
    return JsonResponse(False, safe=False)


@csrf_exempt
def dislike(request): # use 1,2,3 to indicate the state of dislike
    # Dont worry about the likes/dislikes count. They are dislayed through Models.Post
    
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
   
    usr = request.user.id
    post_id = data.get("postid","")

    postid = Post.objects.get(id=post_id)
    disliker = User.objects.get(id=usr)
    post = Post.objects.get(id= post_id)

    
    fetch_post = Like.objects.filter(main_user = post.user, post_like_user = disliker,post_id = postid)
    
    
    print(fetch_post.count())

    # 1 = to indicate that post has no diliked by the current user
    # 2 = to indicate that post has already been diliked by the current user


    ind = 0  
    if (fetch_post.count() ==0):
        ind = 1

    elif(fetch_post.count() >0 and fetch_post[0].user_liked == True): # previoulsy use liked the post he want to dislike it.
        ind = 2
    elif(fetch_post.count() >0 and fetch_post[0].user_liked == True): # already liked the post now undo the like and then dislike it.
        ind =3

  

    
    if (ind == 1 ):
        dislike_post = Like.objects.create(main_user = post.user, post_like_user = disliker,post_id = postid,user_disliked = True)
        dislike_post.save()

    elif (ind == 2 ):

        Like.objects.filter(main_user = post.user, post_like_user = disliker,post_id = postid).update(user_disliked = True,user_liked=False)
    elif (ind ==3 ):

        Like.objects.filter(main_user = post.user, post_like_user = disliker,post_id = postid).delete()
        Like.objects.filter(main_user = post.user, post_like_user = disliker,post_id = postid).update(user_disliked = True,user_liked=False)

    else:
        print("already liked")
  
    return JsonResponse({"message": "Post updated successfully!!!"}, status=201)

@csrf_exempt
def undislike(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
   
    usr = request.user.id
    post_id = data.get("postid","")

    postid = Post.objects.get(id=post_id)
    disliker = User.objects.get(id=usr)
    post_onwer_id = Post.objects.get(id= post_id)

    
    Like.objects.filter(main_user = post_onwer_id.user, post_like_user = disliker,post_id = postid,user_disliked=True).delete()
  
    return JsonResponse({"message": "Post updated successfully!!!"}, status=201)

def custom_404(request, exception=None):
    return render(request, 'network/custom_404.html', status=404)