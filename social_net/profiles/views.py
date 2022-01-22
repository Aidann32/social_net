from django.core.files.base import File
from django.shortcuts import render,redirect
from .models import Profile,Relationship
from .forms import ProfileModelForm
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.db.models import Q

def my_profile_view(request):
    user_obj=Profile.objects.get(user=request.user)
    form=ProfileModelForm(request.POST or None,request.FILES or None,instance=user_obj)
    confirm=False
    if request.method=='POST':
        if form.is_valid():
            form.save()
            confirm=True
    context={
        'user_obj':user_obj,
        'form':form,
        'confirm':confirm,
    }
    return render(request,'profiles/my_profile.html',context)

def invites_received_view(request):
    user_obj=Profile.objects.get(user=request.user)
    qs=Relationship.objects.invitations_received(receiver=user_obj)

    context={'qs':qs,}
    return render(request,'profiles/my_invites.html',context)

def invite_profile_list_view(request):
    user=request.user
    qs=Profile.objects.get_all_profiles_to_invite(user)
    context={'qs':qs,}
    return render(request,'profiles/to_invite_list.html',context)

def profile_list_view(request):
    user=request.user
    qs=Profile.objects.get_all_profiles(user)
    context={'qs':qs,}
    return render(request,'profiles/profiles_list.html',context)

class ProfileListView(ListView):
    model=Profile
    template_name='profiles/profiles_list.html'
    context_object_name='qs'

    def get_queryset(self):
        qs=Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        user=User.objects.get(username__iexact=self.request.user)
        profile=Profile.objects.get(user=user)
        context['profile']=profile
        receiver=Relationship.objects.filter(sender=profile)
        sender=Relationship.objects.filter(receiver=profile)
        rel_receiver=[]
        rel_sender=[]
        for item in receiver:
            rel_receiver.append(item.receiver.user)
        for item in sender:
            rel_sender.append(item.sender.user)
        context['rel_receiver']=rel_receiver
        context['rel_sender']=rel_sender
        context["is_empty"]=False
        if len(self.get_queryset())==0:
            context['is_empty']=True
        return context

def send_invitation(request):
    if request.method == 'POST':
        pk=request.POST.get('profile_pk')
        user=request.user
        sender=Profile.objects.get(user=user)
        receiver=Profile.objects.get(pk=pk)

        rel=Relationship.objects.create(sender=sender,receiver=receiver,status='send')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:myprofile')

def remove_from_friends(request):
    if request.method=='POST':
        pk=request.POST.get('profile_pk')
        user=request.user
        sender=Profile.objects.get(user=user)
        receiver=Profile.objects.get(pk=pk)

        rel=Relationship.objects.get((Q(sender=sender)&Q(receiver=receiver)) | 
        (Q(sender=receiver)& Q(receiver=sender)))
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('profiles:myprofile')