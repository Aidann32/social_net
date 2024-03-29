from django.shortcuts import render,redirect
from .models import Post,Like
from profiles.models import Profile
from .forms import PostModelForm,CommentModelForm
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

@login_required 
def post_comment_and_create_list_view(request):
    posts=Post.objects.all().order_by('created_at')
    profile=Profile.objects.get(user=request.user)

    post_added=False
    post_form=PostModelForm()
    comment_form=CommentModelForm()

    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if 'submit_post' in request.POST:
            post_form=PostModelForm(request.POST,request.FILES)
            if post_form.is_valid():
                instance=post_form.save(commit=False)
                instance.author=profile
                instance.save()
                post_form=PostModelForm()
                post_added=True

        if 'submit_comment' in request.POST:
            comment_form=CommentModelForm(request.POST)
            if comment_form.is_valid():
                instance=comment_form.save(commit=False)
                instance.user=profile
                instance.post=Post.objects.get(id=request.POST.get('post_id'))
                instance.save()
                comment_form=CommentModelForm()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


    context={
        'posts':posts,
        'profile':profile,
        'post_form':post_form,
        'comment_form':comment_form,
        'post_added':post_added,
    }
    return render(request,'posts/main.html',context)

@login_required
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
        
        data={
            'value': like.value,
            'likes':post_obj.liked.all().count()
        }
        return JsonResponse(data,safe=False)
    return redirect('posts:main-post-view')


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    template_name='posts/confirm_delete.html'
    success_url=reverse_lazy('posts:main-post-view')

    def get_object(self,*args,**kwargs):
        pk=self.kwargs.get('pk')
        obj=Post.objects.get(pk=pk)
        if not obj.author.user==self.request.user:
            messages.warning(self.request,"Чтобы удалить этот пост Вы должны являться его автором!")
        return obj

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model=Post
    form_class=PostModelForm
    template_name='posts/update.html'
    success_url=reverse_lazy('posts:main-post-view')
    
    def form_valid(self,form):
        profile=Profile.objects.get(user=self.request.user)
        if form.instance.author==profile:
            return super().form_valid(form)
        else:
            form.add_error(None,"Чтобы изменить этот пост Вы должны являться его автором!")
            return super().form_invalid(form)


