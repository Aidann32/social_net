from django.urls import path
from .views import (
    my_profile_view,
    invites_received_view,
    profile_list_view,
    invite_profile_list_view,
    ProfileListView,
    send_invitation,
    remove_from_friends
)
app_name='profiles'
urlpatterns = [
    path('myprofile/',my_profile_view,name='myprofile'),
    path('invites/',invites_received_view,name='invites-received-view'),
    path('all/',ProfileListView.as_view(),name='all-profile-view'),
    path('to-invite/',invite_profile_list_view,name='invite-profile-view'),
    path('send-invite',send_invitation,name="send-invite"),
    path('remove-friend',remove_from_friends,name="remove-friend")
]

