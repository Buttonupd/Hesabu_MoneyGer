


# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.contrib.auth.models import AbstractUser

#     @receiver(post_save, sender=AbstractUser)
#     def create_user_profile(sender, instance, created, **kwargs):

#             if created:
#                 UserProfile.objects.create(user=instance)
#                 print('profile created')

#     # save user instance
#     @receiver(post_save, sender=AbstractUser)
#     def save_profile(sender, instance, **kwargs):
#             instance.profile.save()
#             print(instance.profile.save())