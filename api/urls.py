from django.urls import path, include
from django.conf.urls import url, re_path
from . import views
from rest_auth.registration.views import VerifyEmailView
from allauth.account.views import PasswordChangeView
from rest_framework.routers import DefaultRouter

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
  
]
