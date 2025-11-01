from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from gyms.models import Gym

@receiver(post_save, sender=User)
def create_gym_for_owner(sender, instance, created, **kwargs):
    if created and instance.role == User.Roles.OWNER and not instance.gym:
        gym = Gym.objects.create(name=f"{instance.username} Gym", owner=instance)
        instance.gym = gym
        instance.save()
