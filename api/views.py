from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from api.models import User, Profile, Education, Experience
from api.serializers import UserSerializer, ProfileSerializer, EducationSerializer,ExperienceSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
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

class UserDetail(APIView):
    model_class = User
    serializer_class = UserSerializer
    head = "user"

    def get_object(self, pk):
        try:
            return self.model_class.objects.get(pk=pk)    
        except self.model_class.DoesNotExist:
            raise ValidationError({
                'status': False,
                'message': f"failed to find {self.head}",
                "data": {}
            })

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj)
        return Response(
            data={
                "status": True,
                "message": f"{self.head} data reterived sucessfully",
                "data": serializer.data
            })

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "status": True,
                    "message": f"{self.head} updated sucessfully",
                    "data": serializer.data
                })
        return Response(data={
            "status": False,
            "message": f"{self.head} update failed",
            "data": serializer.errors
        },
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "status": True,
                    "message": f"{self.head} updated sucessfully",
                    "data": serializer.data
                })
        return Response(data={
            "status": False,
            "message": f"{self.head} update failed",
            "data": serializer.errors
        },
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(data={
            "status": True,
            "message": f"{self.head} deleted sucessfully",
            "data": {}
        },
                        status=status.HTTP_200_OK)

class ProfileList(generics.ListCreateAPIView): 
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"true","message":"data Posted succesfully.","data":{"uuid": serializer.data['uuid']}}, status=status.HTTP_201_CREATED)
        return Response({'message': 'user with this email already exist',}, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetails(APIView):
    model_class = Profile
    serializer_class = ProfileSerializer
    head = "developer profile"

    def get_object(self, pk):
        try:
            return self.model_class.objects.get(pk=pk)
        except self.model_class.DoesNotExist:
            raise ValidationError({
                'status': False,
                'message': f"failed to find {self.head}",
                "data": {}
            })

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = DeveloperProfileSerializerRead(obj)
        return Response(
            data={
                "status": True,
                "message": f"{self.head} reterived sucessfully",
                "data": serializer.data
            })

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data)

        user_data = {}
        if request.data.get("first_name"):
            user_data["first_name"] = request.data.get("first_name")
        if request.data.get("last_name"):
            user_data["last_name"] = request.data.get("last_name")

        if User.objects.filter(pk=pk).exists():
            user_obj = User.objects.get(pk=pk)
            user_serializer = UserSerializer(user_obj,
                                             data=user_data,
                                             partial=True)

            if user_serializer.is_valid():
                user_serializer.save()

        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "status": True,
                    "message": f"{self.head} updated sucessfully",
                    "data": serializer.data
                })
        return Response(data={
            "status": False,
            "message": f"{self.head} update failed",
            "data": serializer.errors
        },
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj,
                                           data=request.data,
                                           partial=True)

        user_data = {}
        if request.data.get("first_name"):
            user_data["first_name"] = request.data.get("first_name")
        if request.data.get("last_name"):
            user_data["last_name"] = request.data.get("last_name")

        if User.objects.filter(pk=pk).exists():
            user_obj = User.objects.get(pk=pk)
            user_serializer = UserSerializer(user_obj,
                                             data=user_data,
                                             partial=True)

            if user_serializer.is_valid():
                user_serializer.save()

        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "status": True,
                    "message": f"{self.head} updated sucessfully",
                    "data": serializer.data
                })
        return Response(data={
            "status": False,
            "message": f"{self.head} update failed",
            "data": serializer.errors
        },
                        status=status.HTTP_400_BAD_REQUEST)




'''
class ProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        profile_serializer = ProfileSerializer(user.profile)
        return Response(profile_serializer.data)

'''