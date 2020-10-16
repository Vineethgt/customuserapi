from api.models import User, Profile, Education, Experience, Feed
from api.serializers import UserSerializer, ProfileSerializer, EducationSerializer, ExperienceSerializer, FeedSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
from .Base_Viewset import BaseViewset
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters 
import rest_framework.mixins as mixin
from rest_framework.filters import SearchFilter, OrderingFilter
from url_filter.integrations.drf import DjangoFilterBackend
#from .filter import ProfileFilter, EducationFilter, ExperienceFilter
import django_filters


class BasicPagination(PageNumberPagination):
    page_size_query_param = '2'

class UserViewset(BaseViewset):
    model_class = User
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
    ordering_fields =('name','email')
    filter_fields = ('name', 'email','created_at')
    search_fields = ('name','email')
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = BasicPagination
    head = "user"
    


class ProfileViewset(BaseViewset):
    model_class = Profile
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
    ordering_fields =('bio','city')
    filter_fields = ('bio', 'city','created_at')
    search_fields = ('bio', 'city')
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    pagination_class = BasicPagination
    head = "profile"

class EducationViewset(BaseViewset):
    model_class = Education
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    #filter_fields = {'university':['exact'], 'degree':['exact'],'start_date':['gte'],'end_date':['lte']}
    filter_fields = ('university', 'degree','start_date','end_date')
    search_fields = ('university', 'degree')
    serializer_class = EducationSerializer
    queryset = Education.objects.all()
    pagination_class = BasicPagination
    head = "education"

class ExperienceViewset(BaseViewset):
    model_class = Experience
    filter_backends = [filters.SearchFilter, DjangoFilterBackend,]
    filter_fields = ('title', 'company','start_date','end_date') #start_date__gte & end_date__lte
    search_fields = ('title', 'company')
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    pagination_class = BasicPagination
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

