from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main', views.main, name='main2'),
    path('post-tweet', views.post_tweet, name='post-tweet'),
    path('reply/<int:id>/', views.reply, name='reply'),
    path('tweet-detail/<int:id>/', views.tweet_detail, name='tweet-detail'),
    path('add-tweet', views.tweet_post, name='tweet-post'),
    path('reply/<int:id>/add-reply', views.tweet_post, name='tweet-post')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
