import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from api.UserManager import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    uuid            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email           = models.EmailField(verbose_name="email_address",max_length=300,unique=True)
    password        = models.CharField(max_length=200,verbose_name='password')
    name            = models.CharField(max_length=200,null=True)
    date_of_birth   = models.DateField(verbose_name='date_of_birth',blank=True,default=None,null=True)
    created_at      = models.DateTimeField(verbose_name="created_at",blank=True,null=True,auto_now_add=True)
    updated_at      = models.DateTimeField(verbose_name="updated_at",blank=True,null=True,auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager

    def __str__(self):
        return self.email

















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