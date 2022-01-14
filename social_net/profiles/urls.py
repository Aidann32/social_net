from django.urls import path
from .views import my_profile_view,invites_received_view,profile_list_view,invite_profile_list_view
app_name='profiles'
urlpatterns = [
    path('myprofile/',my_profile_view,name='myprofile'),
    path('invites/',invites_received_view,name='invites-received-view'),
    path('all/',profile_list_view,name='all-profile-view'),
    path('to-invite/',invite_profile_list_view,name='invite-profile-view')
]

