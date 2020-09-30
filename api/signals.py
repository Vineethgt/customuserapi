from django.db.models.signals import post_save
from accounts.models import User , profile
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.objects.save()

