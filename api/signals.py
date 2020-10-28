from django.db.models.signals import post_save
from .models import User , profile, Education, Experience, Feed, FriendRequest
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.objects.save()

@receiver(post_save, sender=FriendRequest)
def create_or_update_user_friendrequest(sender, instance, created, **kwargs):
    if created:
        FriendRequest.objects.create(user=instance)


@receiver(post_save, sender=FriendRequest)
def save_follow(sender, instance, **kwargs):
    FriendRequest.objects.save()
