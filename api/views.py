from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from api.models import User, Profile, Education, Experience, Feed
from api.serializers import UserSerializer, ProfileSerializer, EducationSerializer, ExperienceSerializer, FeedSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .baseview import BaseDetails
import uuid



class UserList(generics.ListCreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"true","message":"data Posted succesfully.","data":{"uuid": serializer.data['uuid']}}, status=status.HTTP_201_CREATED)
        return Response({'message': 'user with this email already exist',}, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(BaseDetails):
    model_class = User
    serializer_class = UserSerializer
    head = "user"


class ProfileDetail(BaseDetails):
    model_class = Profile
    serializer_class = ProfileSerializer
    head = "profile"

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, **kwargs):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many = True)
        return Response({"status": "true", "message": "data Retrieve successfully.", "data": serializer.data})

class EducationDetail(BaseDetails):
    model_class = Education
    serializer_class = EducationSerializer
    head = "education"

class EducationList(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    def get(self, request, **kwargs):
        education = Education.objects.all()
        serializer = EducationSerializer(education, many = True)
        return Response({"status": "true", "message": "data Retrieve successfully.", "data": serializer.data})

class ExperienceDetail(BaseDetails):
    model_class = Experience
    serializer_class = ExperienceSerializer
    head = "experience"

class ExperienceList(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get(self, request, **kwargs):
        experience = Experience.objects.all()
        serializer = ExperienceSerializer(experience, many = True)
        return Response({"status": "true", "message": "data Retrieve successfully.", "data": serializer.data})

class Feedpage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def get(self, request, **kwargs):
        fed = Feed.objects.all()
        serializer = FeedSerializer(fed, many=True)
        return Response({"status": "true", "message": "data Retrieve successfully.", "data": serializer.data})



'''
class ProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        profile_serializer = ProfileSerializer(user.profile)
        return Response(profile_serializer.data)

'''