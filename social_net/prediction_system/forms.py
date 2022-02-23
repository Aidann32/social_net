from django import forms
from .models import ProfileData
from profiles.models import Profile
class ProfileDataForm(forms.ModelForm):
    class Meta:
        model=ProfileData
        exclude=('prediction','profile')


    # def is_valid(self,*args,**kwargs):
    #     if self.profile:
    #         super(ProfileDataForm, self).is_valid(*args,**kwargs)
    #     return False
    
    # def __init__(self,*args,**kwargs):
    #     super(ProfileDataForm, self).__init__(*args, **kwargs)
       
