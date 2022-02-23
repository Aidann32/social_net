from .models import ProfileData
from profiles.models import Profile

def has_prediction(request):
    if request.user.is_authenticated:
        profile=Profile.objects.get(user=request.user)
        if ProfileData.objects.filter(profile=profile).exists():
            return {'has_prediction': True}
    return {'has_prediction': False}