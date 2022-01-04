from django.shortcuts import render
from .models import Profile
def my_profile_view(request):
    user_obj=Profile.objects.get(user=request.user)
    context={
        'user_obj':user_obj,
    }
    return render(request,'profiles/profiles.html',context)