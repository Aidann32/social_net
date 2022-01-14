from django.core.files.base import File
from django.shortcuts import render
from .models import Profile,Relationship
from .forms import ProfileModelForm

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

def profile_list_view(request):
    user=request.user
    qs=Profile.objects.get_all_profiles(user)
    context={'qs':qs,}
    return render(request,'profiles/profiles_list.html',context)

def invite_profile_list_view(request):
    user=request.user
    qs=Profile.objects.get_all_profiles_to_invite(user)
    context={'qs':qs,}
    return render(request,'profiles/to_invite_list.html',context)

