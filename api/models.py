import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from api.UserManager import UserManager
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class BaseModel(models.Model):
    uuid            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at      = models.DateTimeField(verbose_name="created_at",blank=True,null=True,auto_now_add=True)
    updated_at      = models.DateTimeField(verbose_name="updated_at",blank=True,null=True,auto_now=True)

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
    user               = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image      = models.ImageField(default=None,upload_to='profile_pics')
    bio                = models.CharField(default=None,max_length=500)
    headline           = models.CharField(default=None,max_length=100)
    date_of_birth      = models.DateField(verbose_name='date_of_birth',blank=True,default=None,null=True)
    gender             = models.CharField(max_length=1, blank=True, null=True)
    city               = models.CharField(max_length=20, blank=True, null=True)
    country            = models.CharField(max_length=20, null=True, blank=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.TextField(default=False)
    def __str__(self):
        return f'{self.user.email} Feed'

    


















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