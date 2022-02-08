from .models import Profile,Relationship

def profile_pic(request):
    if request.user.is_authenticated:
        profile_picture=Profile.objects.get(user=request.user).avatar_image
        return {'avatar_pic':profile_picture}
    return {}

def invitations_number(request):
    if request.user.is_authenticated:
        profile_obj=Profile.objects.get(user=request.user)
        qs_counter=Relationship.objects.invitations_received(profile_obj).count()
        return {'invites_num':qs_counter,}
    return {}

