from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from student.models import Student


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
