from django.urls import path
from .views import post_comment_and_create_list_view,like_unlike_post

app_name='posts'

urlpatterns=[
    path('',post_comment_and_create_list_view,name='main-post-view'),
    path('like',like_unlike_post,name='like-post-view')
]