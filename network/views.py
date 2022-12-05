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
        'placeholder': 'Your two cents'
    }))
    image = forms.ImageField(required=False)


def like(request, postId):
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
    if request.method == 'PUT':
        row = Post.objects.filter(id=postId)
        totalLikes = getattr(row, 'totalLikes')
        Post.objects.filter(id=postId).update(totalLikes=totalLikes + 1)

    if request.method == 'POST':
        like = Likes.objects.create_likes(
            username=request.username, post=postId)
        like.save()
    return JsonResponse({'successful': 'Liked'})


def dislike(request, postId):
    pass


def comment(request, postId):
    pass


def index(request):
    posts = Post.objects.all().values()
    posts = Paginator(posts, 10)
    print(posts.page(1).object_list)
    if posts.num_pages <= 5:
        return render(request, "network/index.html", {
            'postForm': PostForm,
            'numPages': posts.num_pages,
            'posts': posts.page(1).object_list,
        })
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data['image'])
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

    return render(request, "network/index.html", {
        'postForm': PostForm,
        'numPages': posts.num_pages,
        'posts': posts.page(1).object_list,
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
            user = User.objects.create_user(username, email, password)
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
