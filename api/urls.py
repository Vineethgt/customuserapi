"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url, re_path
from . import views
from rest_auth.registration.views import VerifyEmailView
from allauth.account.views import PasswordChangeView


app_name='api'

urlpatterns = [
    path('users/', views.UserList.as_view(),name='user-list'),
    path('users/<uuid:pk>/', views.UserDetails.as_view(),name='user-detail'),
    path('profile/', views.ProfileList.as_view(),name='profile-list'),
    path('profile/<uuid:pk>/',views.ProfileDetail.as_view(),name='profile-detail'),
    path('education/',views.EducationList.as_view(),name='education-list'),
    path('education/<uuid:pk>/',views.EducationDetail.as_view(),name='education-detail'),
    path('experience/',views.ExperienceList.as_view(),name='education-list'),
    path('experience/<uuid:pk>/',views.ExperienceDetail.as_view(),name='education-detail'),
    path('feedpage/',views.Feedpage.as_view(),name='Feed-Detail'),
    path('sendm/',views.email,name='send-email'),

    path('account/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),


    
]


#path('users/<int:pk>/profile/', views.ProfileAPI.as_view())

'''router = routers.DefaultRouter()
router.register(r'users', views.UserList)
router.register(r'userdetail', views.UserDetail)

urlpatterns = [
    path('users/',include)
]
'''