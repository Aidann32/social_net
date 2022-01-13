from django.core.files.base import File
from django.shortcuts import render
from .models import Profile
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