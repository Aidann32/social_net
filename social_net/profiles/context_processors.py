from .models import Profile

def profile_pic(request):
    if request.user.is_authenticated:
        profile_picture=User.objects.get(user=request.user).avatar_image
        return {'avatar_pic':profile_picture}
    return {}
