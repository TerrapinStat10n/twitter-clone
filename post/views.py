import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import TwitterDjango
# Create your views here.


def main(request):
    user_post = TwitterDjango.objects.filter(parent_tweet_id=0).order_by('-created_at')

    context = {
        'posts': user_post
    }
    return render(request, 'home.html', context)


def post_tweet(request):
    return render(request, 'post-tweet.html')


def reply(request, id):
    user_post = TwitterDjango.objects.filter(pk=id)

    context = {
        'posts': user_post,

    }
    return render(request, 'reply.html', context)


def tweet_detail(request, id):
    user_post = TwitterDjango.objects.filter(pk=id)
    user_reply = TwitterDjango.objects.filter(parent_tweet_id=id)

    context = {
        'posts': user_post,
        'replies': user_reply
    }

    return render(request, 'tweet-detail.html', context)


def tweet_post(request, id=0):
    name = request.POST.get("name")
    text = request.POST.get("text")
    image = request.FILES.get("photo", None)
    parent_tweet_id = id


    if image:
        with open('post/static/post/user_images/' + str(image), 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        image_path = 'post/user_images/' + str(image)
    else:
        image_path = None

    post = TwitterDjango(name=name, text=text, image_path=image_path, parent_tweet_id=parent_tweet_id)
    post.save()

    return redirect(reverse('main'))
