from django.urls import path
from .views import (
    my_profile_view,
    invites_received_view,
    profile_list_view,
    invite_profile_list_view,
    ProfileListView,
    ProfileDetailView,
    send_invitation,
    remove_from_friends,
    accept_invitation,
    reject_invitation,
    friend_search_view,
)
app_name='profiles'
urlpatterns = [
    path('',ProfileListView.as_view(),name='all-profile-view'),
    path('myprofile/',my_profile_view,name='myprofile'),
    path('invites/',invites_received_view,name='invites-received-view'),
    path('to-invite/',invite_profile_list_view,name='invite-profile-view'),
    path('send-invite',send_invitation,name="send-invite"),
    path('remove-friend',remove_from_friends,name="remove-friend"),
    path('<slug>/',ProfileDetailView.as_view(),name='profile-detail-view'),
    path('invites/accept',accept_invitation,name="accept-invite"),
    path('invites/reject',reject_invitation,name="reject-invite"),
    path('friends/search',friend_search_view,name="friend-search")
]

