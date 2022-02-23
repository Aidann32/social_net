from django.shortcuts import render
from .models import ProfileData
from .forms import ProfileDataForm
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import Http404

@login_required
def index(request):
    profile=Profile.objects.get(user=request.user)
    if ProfileData.objects.filter(profile=profile).exists():
        raise Http404
    form=ProfileDataForm()
    if request.method == 'POST':
        form=ProfileDataForm(request.POST or None)
        if form.is_valid():
            new_data=form.save(commit=False)
            new_data.profile=profile
            new_data.save()

    return render(request, 'prediction/index.html',{'form':form,})

@login_required
def prediction_detail(request):
    try:
        profile=Profile.objects.get(user=request.user)
        profile_data=ProfileData.objects.get(profile=profile)
        return render(request, 'prediction/prediction_detail.html',{
            'prediction':profile_data.prediction,})
    except Exception as e:
        print(e)
        raise Http404
