from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from allauth.account.views import confirm_email


urlpatterns = [
    path('',include('api.urls')),
    path('admin/', admin.site.urls),
    path('api/token',TokenObtainPairView.as_view()),
    path('api/token/refresh',TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^accounts/', include('allauth.urls')),

]
