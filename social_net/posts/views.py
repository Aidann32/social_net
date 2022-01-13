from django.shortcuts import render,redirect
from .models import Post,Like
from profiles.models import Profile

def post_comment_and_create_list_view(request):
    posts=Post.objects.all()
    profile=Profile.objects.get(user=request.user)
    context={
        'posts':posts,
        'profile':profile
    }
    return render(request,'posts/main.html',context)

def like_unlike_post(request):
    user=request.user
    if request.method=='POST':
        post_id=request.POST.get('post_id')
        post_obj=Post.objects.get(id=post_id)
        profile=Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
        
        like,created=Like.objects.get_or_create(user=profile,post_id=post_id)
        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'
        post_obj.save()
        like.save()
        return redirect('posts:main-post-view')