from django.urls import path
from .views import post_comment_and_create_list_view,like_unlike_post,PostDeleteView,PostUpdateView

app_name='posts'

urlpatterns=[
    path('',post_comment_and_create_list_view,name='main-post-view'),
    path('like',like_unlike_post,name='like-post-view'),
    path('<int:pk>/delete',PostDeleteView.as_view(),name='delete-post'),
    path('<int:pk>/update',PostUpdateView.as_view(),name='update-post'),
]