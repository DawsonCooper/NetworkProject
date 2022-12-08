from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django import forms
from django.db import models
from .models import User, Post, Likes, Comment
from django.core.paginator import Paginator


class PostForm(forms.Form):
    caption = forms.CharField(widget=forms.Textarea(attrs={
        'cols': '40',

    }))
    image = forms.ImageField(required=False)

# API VIEWS


@csrf_exempt
def get_post_data(request, postId):
    postData = Post.objects.filter(id=postId).values()

    ready = postData[0]['caption']
    print(ready)
    # return JsonResponse(caption=postData.caption, safe=False)
    return JsonResponse({
        'caption': ready
    })


@csrf_exempt
def create_realationship(request, user):
    """WE COULD POSSIBLY RECIEVE 3 REQUESTS POST TO CREATE A NEW REALATIONSHIP
        PUT WE WILL WANT TO DELETE THE ENTIRE ROW OF A REALATIONSHIP
        GET WE WILL WANT TO RETURN A GIVEN USERS FOLLOWERS AND FOLLOWING 
    """
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        pass

    if request.method == 'PUT':
        pass

    pass


@csrf_exempt
def get_user_interactions(request):
    interactions = Likes.objects.filter(username=request.user)

    return JsonResponse([interaction.serialize() for interaction in interactions], safe=False)


@csrf_exempt
def update_post(request, postId):

    caption = json.loads(request.body)
    caption = caption.get('body')
    Post.objects.filter(id=postId).update(caption=caption)


@csrf_exempt
def interaction_API(request, postId):
    try:
        post = Post.objects.get(id=postId)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post no longer exists"})
    if request.method == 'GET':
        likes = Likes.objects.filter(post=postId).values()
        for like in likes:
            like.serialize()
            user = like.get_user()
            like.append(user)
        print(likes)
        return JsonResponse(likes)

    if request.method == 'POST':
        # UPDATE THE LIKES MODEL TO TRACK WHO HAS LIKED THE POST
        data = json.loads(request.body)
        interaction = data.get('body')
        print('interaction', interaction)
        updateLike = True
        statusValue = 0
        if interaction == 'like':
            statusValue = 1
        elif interaction == 'dislike':
            statusValue = -1
        elif interaction == 'undo':
            statusValue = 0
        try:
            updateLike = Likes.objects.get(post=postId, username=request.user)
        except Likes.DoesNotExist:
            like = Likes(
                username=request.user,
                post=postId,
                status=statusValue)
            like.save()
            return JsonResponse({'successful': 'Liked'})

        updateLike.status = statusValue
        updateLike.save()
        if statusValue == 0 and interaction != 'undo':
            # THIS WILL BE FOR OUT COMMENTS AND WE WILL BE MODIFYING THE COMMMENT MODEL

            pass
        # UPDATE POST MODEL TO TRACK NUM OF LIKES
        row = Post.objects.filter(id=postId).values()
        totalLikes = row[0]['totalLikes']
        if statusValue == 1:
            Post.objects.filter(id=postId).update(totalLikes=totalLikes + 1)
        elif statusValue == -1:
            Post.objects.filter(id=postId).update(totalLikes=totalLikes - 1)
        else:
            pass
    return JsonResponse({'successful': 'Liked'})


def index(request):

    posts = Post.objects.all().values()
    posts = posts.order_by("-timestamp").all()
    posts = Paginator(posts, 10)
    print(request)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                username=request.user,
                caption=form.cleaned_data['caption'],
                image=form.cleaned_data['image'],
            )
            post.save()
        return render(request, "network/index.html", {
            'postForm': PostForm,
            'numPages': posts.num_pages,
            'posts': posts.page(1).object_list,
        })
    if posts.num_pages <= 5:
        return render(request, "network/index.html", {
            'postForm': PostForm,
            'numPages': posts.num_pages,
            'posts': posts.page(1).object_list,

        })
    return render(request, "network/index.html", {
        'postForm': PostForm,
        'numPages': posts.num_pages,
        'posts': posts.page(1).object_list,


    })


def profile(request, username):
    userPosts = Post.objects.filter(username=username).all().values()
    userInfo = User.objects.filter(username=username).values()

    return render(request, "network/profile.html", {
        'postForm': PostForm,
        'userPosts': userPosts,
        'userInfo': userInfo[0]
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        # Check if authentication successful
        if user is not None:

            login(request, user)
            return index(request)
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
        name = request.POST["name"]
        email = request.POST["email"]
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            bio = form.cleaned_data["caption"]
            profilePic = form.cleaned_data["image"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match.",
                'postForm': PostForm,
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username, email, password, name, bio)
            user.save()
            if profilePic != None:
                test = User.objects.filter(username=username, password=password).update(
                    bio=bio,
                    profilePic=profilePic,
                )
            else:
                test = User.objects.filter(username=username, password=password).update(
                    bio=bio,

                )
                test.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken.",
                'postForm': PostForm,
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html", {
            'postForm': PostForm,
        })
