from django.db.models.signals import post_save
from users.models import CustomUser
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Profile.objects.create(user=instance)
        pass


@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    pass
    #  instance.profile.save()
