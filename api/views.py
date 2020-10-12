from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from api.models import User, Profile, Education, Experience, Feed
from api.serializers import UserSerializer, ProfileSerializer, EducationSerializer, ExperienceSerializer, FeedSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect, request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .Base_Viewset import BaseViewset
import uuid
from django.core.mail import send_mail
from django.conf import settings
from api.pagination import PaginationHandlerMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

class BasicPagination(PageNumberPagination):
    page_size_query_param = '2'

class UserViewset(BaseViewset):
    model_class = User
    pagination_class = BasicPagination
    serializer_class = UserSerializer
    queryset = User.objects.all()
    head = "user"


class ProfileViewset(BaseViewset):
    model_class = Profile
    pagination_class = BasicPagination
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    head = "profile"

class EducationViewset(BaseViewset):
    model_class = Education
    pagination_class = BasicPagination
    serializer_class = EducationSerializer
    queryset = Education.objects.all()
    head = "education"

class ExperienceViewset(BaseViewset):
    model_class = Experience
    pagination_class = BasicPagination
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    head = "experience"

class FeedViewset(BaseViewset):
    queryset = Feed.objects.all()
    pagination_class = BasicPagination
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()
    head = "feed"

def email(request):

    subject = 'Thank you for registering'
    message = 'It means a world to us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['vineeth.t@engineerbabu.in']

    send_mail(subject,message,email_from, recipient_list)

    return HttpResponseRedirect('http://127.0.0.1:8000/users/')

