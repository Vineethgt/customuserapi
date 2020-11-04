from django.urls import path, include
from django.conf.urls import url, re_path
from django.contrib import admin
from . import views 
from rest_auth.registration.views import VerifyEmailView
from allauth.account.views import PasswordChangeView
from rest_framework.routers import DefaultRouter
from django.conf import  settings

app_name='api'

router = DefaultRouter()
router.register(r'user', views.UserViewset)
router.register(r'profile', views.ProfileViewset)
router.register(r'education', views.EducationViewset)
router.register(r'experience', views.ExperienceViewset)
router.register(r'feed', views.FeedViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('account/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),


    # users
    path("users/follow/<uuid:uid>/", views.Follow.as_view(), name="follow"),
    path("users/unfollow/<uuid:uid>/", views.Unfollow.as_view(), name="unfollow"),
    path("users/followers/", views.ListFollowers.as_view(), name="followers"),
    path("users/following/", views.ListFollowing.as_view(), name="following"),
    path("users/friendrequests/<uuid:uid>/", views.SendFriendRequest.as_view(), name="send-friend-request"),
    path('friendrequests/', views.ShowPendingReceivedFriendRequests.as_view(), name="show-pending-received-fr-request"),
    path('friendrequests/pending/', views.ShowPendingSentFriendRequests.as_view(), name="show-pending-sent-fr-request"),
    path("users/friendrequests/accept/<uuid:request_id>/", views.AcceptFriendRequest.as_view(), name="accept-friend-request"),
   
]
