from django.shortcuts import render
from rest_framework import generics
from api.models import User
from api.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        profile_serializer = ProfileSerializer(user.profile)
        return Response(profile_serializer.data)