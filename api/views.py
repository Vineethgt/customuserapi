from api.models import User, Profile, Education, Experience, Feed, FriendRequest
from api.serializers import UserSerializer, ProfileSerializer, EducationSerializer, ExperienceSerializer, FeedSerializer, FriendRequestSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView, GenericAPIView, CreateAPIView
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
from django.contrib.auth import  get_user_model
import django_filters
from django.core.mail import EmailMessage

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

#######################################################Followrequest###################################################################

# POST: follow a user
class Follow(UpdateAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = "uid"

    def patch(self, request, *args, **kwargs):
        uid = self.kwargs.get("uid")
        user_to_follow = User.objects.__getattribute__(uuid=uid)
        user_to_follow.followed_by.add(self.request.user.user_profile)       
        return Response(f"{self.email} follows {user_to_follow.email}")

# POST: unfollow a user
class Unfollow(DestroyAPIView):
    queryset = UserSerializer
    serializer_class = ProfileSerializer
    lookup_url_kwarg = "uid"

    def delete(self, request, *args, **kwargs):
        uid = self.kwargs.get("uid")
        to_delete = User.objects.get(uuid=uid)
        self.request.user.user_profile.follow.remove(to_delete)
        return Response("Unfollowed!")


# GET: List of all the followers
class ListFollowers(ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        followers_profile = self.request.user.followed_by.all()
        return [up.parent_user for up in followers_profile]


# GET: List of all the people the user is following
class ListFollowing(ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        following_profiles = self.request.user.user_profile.follow.all()
        return following_profiles

###########################################################FriendRequests###############################################################

# POST: Send friend request to user
class SendFriendRequest(GenericAPIView):
    serializer_class = FriendRequestSerializer
    lookup_url_kwarg = "uid"

    def post(self, request, *args, **kwargs):
        receiver_id = kwargs["uid"]
        receiver = User.objects.get(uuid=receiver_id)
        if self.request.user.email != receiver.email:
            friend_request, created = FriendRequest.objects.create(sender=self.request.user, receiver=receiver)
            if created:
                return Response(f"{self.request.user.email} sent a friend request to {receiver.email}")
            else:
                return Response(f"You have already sent a friend request to {receiver.email}")
        return Response(f"You can't send a friend request to yourself, {self.request.user.email}")


# GET: List all open friend requests from others
class ShowPendingReceivedFriendRequests(ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        received_requests = FriendRequest.objects.filter(status="pending", receiver_id=self.request.user.uuid)
        return received_requests


# GET: List all my pending friend requests
class ShowPendingSentFriendRequests(ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        sent_requests = FriendRequest.objects.filter(status="pending", sender_id=self.request.user.uuid)
        return sent_requests


# POST: Accept an open friend request
class AcceptFriendRequest(GenericAPIView):
    serializer_class = FriendRequestSerializer
    lookup_url_kwarg = "request_id"

    def post(self, request, *args, **kwargs):
        request_id = kwargs["request_id"]
        try:
            friend_request = FriendRequest.objects.get(uuid=request_id)
            sender = User.objects.get(uuid=friend_request.sender_id)
            receiver = User.objects.get(uuid=friend_request.receiver_id)
            if friend_request.status == "pending" and self.request.user.uuid == receiver.uuid:
                FriendRequest.objects.create(sender=receiver, receiver=sender, status="friends")
                friend_request.status = "friends"
                friend_request.save()
                return Response(f"{sender.email} and {receiver.email} are now friends!")
            elif friend_request.status == "friends" and self.request.user.uuid == receiver.uuid:
                return Response(f"{sender.email} and {receiver.email} are already friends!")
            else:
                return Response(f"{self.request.user.email} is not part of this friend request.")
        except FriendRequest.DoesNotExist:
            return Response(f"There is no friend request with ID {request_id}")


# DELETE: Reject an open friend request
class RejectFriendRequest(GenericAPIView):
    serializer_class = FriendRequestSerializer
    lookup_url_kwarg = "request_id"

    def delete(self, request, *args, **kwargs):
        request_id = kwargs["request_id"]
        friend_request = FriendRequest.objects.get(uuid=request_id)
        current_user_id = self.request.user.id
        if friend_request.status == "pending" and friend_request.receiver_id == current_user_id:
            friend_request.delete()
            return Response("Friend request was rejected!")
        return Response(f"You have no pending friend request with ID {request_id}")


# GET: List all friends
class ShowFriends(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        accepted_requests = self.request.user.received_friend_request.all().filter(status="friends")
        friends = [fr.sender for fr in accepted_requests]
        return friends


# DELETE: Unfriend a friend
class DeleteFriendRelation(DestroyAPIView):
    serializer_class = FriendRequestSerializer
    lookup_url_kwarg = "uid"

    def delete(self, request, *args, **kwargs):
        user_id = self.kwargs["uid"]
        to_unfriend = User.objects.get(uuid=user_id)
        relation1 = FriendRequest.objects.get(sender=user_id, receiver=self.request.user.id)
        relation2 = FriendRequest.objects.get(sender=self.request.user.id, receiver=user_id)
        relation1.delete()
        relation2.delete()
        return Response(f"{self.request.user.email} unfriended {to_unfriend.email}")

