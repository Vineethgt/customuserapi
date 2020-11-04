import uuid
import jwt
import self as self
from datetime import  timedelta
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from api.UserManager import UserManager
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.utils import timezone
#from django.conf import settings
from django.db.models.functions import datetime
from .UserManager import UserManager
from config import settings


class BaseModel(models.Model):
    uuid            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at      = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at      = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        abstract = True
        
class User(BaseModel,AbstractBaseUser,PermissionsMixin):
    email           = models.EmailField(verbose_name="email_address",max_length=300,unique=True)
    password        = models.CharField(max_length=200,verbose_name='password')
    name            = models.CharField(max_length=200,blank=True,null=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(BaseModel):
    user               = models.OneToOneField(User,on_delete=models.CASCADE, related_name="user_profile")
    profile_image      = models.ImageField(default=None,upload_to='profile_pics', blank= True,null=True)
    bio                = models.CharField(default=None,max_length=500)
    headline           = models.CharField(default=None,max_length=100)
    date_of_birth      = models.DateField(verbose_name='date_of_birth',blank=True,default=None,null=True)
    gender_choice      = [('','Select Gender'),('Male', 'Male'),('Female', 'Female'),('Other', 'Other')]
    gender             = models.CharField(max_length=10, choices=gender_choice, blank=True, null=True)
    city               = models.CharField(max_length=20, blank=True, null=True)
    country            = models.CharField(max_length=20, null=True, blank=True)
    profile_status     = models.CharField(verbose_name="Profile status",max_length=10,choices=(('Public', 'Public'),('Private', 'Private'),),default='Public')
    follow             = models.ManyToManyField(to=User,related_name="followed_by",)
    def __str__(self):
        return f'{self.user.email} Profile'

class Education(BaseModel):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=100)
    degree     = models.CharField(max_length=100)
    major      = models.CharField(max_length=100)
    Score      = models.CharField(default=None,max_length=100)
    start_date = models.DateField(default=None)
    end_date   = models.DateField(default=None)
    def __str__(self):
        return f'{self.user.email} Education'

class Experience(BaseModel):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    title         = models.CharField(max_length=100)
    Field         =  models.CharField(max_length=100)
    company       = models.CharField(max_length=200)
    start_date    = models.DateField(default=None)
    end_date      = models.DateField(default=None)
    work_location = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.user.email} Experience'

class Feed(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    feed = models.TextField(default=False)
    def __str__(self):
        return f'{self.user.email} Feed'


class FriendRequest(BaseModel):
    PENDING = "pending"
    FRIENDS = "friends"
    status = models.CharField(
        verbose_name="status",
        max_length=100,
        choices=(
            (PENDING, PENDING),
            (FRIENDS, FRIENDS),
        ),
        default=PENDING
    )
    sender = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_friend_request"
    )
    receiver = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_friend_request"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.sender} sent friend request to {self.receiver}. Status: {self.status}"




















'''class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='uploads', blank=True)
'''