
# imports
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# class create profile

class UserProfile(models.Model):
    profile_name = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, null=True, related_name='my_profile')
    # email_field = models.EmailField(null=True, unique=True)
    User._meta.get_field('email')._unique = True


    # save user profile
    def __str__(self):
        return str(self.profile_name)

    # model class signal upon creation
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):

            if created:
                UserProfile.objects.create(profile_name=instance)
                print('profile created')

    # save user instance
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
            instance.profile.save()
            print(instance.profile.save())

    # back up
    def save_profile(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print('profile profile')

    # retrieve profiles
    @classmethod
    def get_profile(cls):
        profile = UserProfile.objects.all()
        return profile
# model for data collection

class Project(models.Model):
    MONTH_OF_THE_YEAR = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('Decemeber', 'Decemeber')
    )
    posted_by = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE, related_name='my_user')
    added_month = models.CharField(max_length=10, null=True, blank=False, choices=MONTH_OF_THE_YEAR)
    profile = models.ForeignKey(UserProfile, null=True, blank=False,  on_delete=models.CASCADE, related_name='his_user')
    product = models.CharField(max_length=20, null=True, blank=False )
    product_item = models.CharField(max_length=20, null=True, blank=False )
    quantity = models.IntegerField(null=True, blank=False)
    price = models.IntegerField(null=True, blank=False )
    total = models.IntegerField(editable=True, null=True, blank=False)
    date_created = date_created = models.DateTimeField(auto_now_add=True, null=True, blank=False)

    def __str__(self):
        return str(self.profile)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)

    @classmethod
    def get_projects(cls):
        projects = Project.objects.all()
        return projects

    @classmethod
    def find_project(cls,search_term):
        project = Project.objects.filter(product__icontains=search_term)

        return project

class MadeSale(models.Model):
    MONTH_OF_THE_YEAR = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('Decemeber', 'Decemeber')
    )
    month_of_sales =  models.CharField(max_length=10, null=False, blank=False, choices=MONTH_OF_THE_YEAR)
    juror = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    profile = models.ForeignKey(UserProfile, null=True, blank=False,  on_delete=models.CASCADE, related_name='profile3')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=False)
    margin = models.IntegerField(null=True, blank=False)
    sales = models.IntegerField( null=True, blank=False)
    comment = models.CharField(max_length=200, null=True, blank=False)
    date_created = date_created = models.DateTimeField(auto_now_add=True, null=True, blank=False)

    def __str__(self):
        return str(self.profile)

    def save(self, *args, **kwargs):
        self.margin = self.sales - Project.objects.last().total
        if self.sales > self.margin:

            self.margin =  self.margin
        else:
            -self.margin
        return super().save( *args, **kwargs)

    @classmethod
    def get_sales(cls):
        accounts = MadeSale.objects.all()
        return accounts

class MilkCollection(models.Model):
    Day_Collected = (
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ('saturday', "Saturday"),
        ('sunday', "Sunday"),
    )

    juror = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(UserProfile, null=True, blank=False,  on_delete=models.CASCADE, related_name='profile2')
    day_of_the_week = models.CharField(choices=Day_Collected, max_length=10)
    morning_litres = models.FloatField(null=True, default=0.00)
    evening_litres = models.FloatField(null=True, default=0.00)
    total_litres = models.FloatField(null=True, default=0.00)
    price_per_litre = models.FloatField(max_length=30, null=True, blank=False)
    price_per_month = models.FloatField(null=True)
    total = models.FloatField(null=True)

    def __str__(self):
        return str(self.profile)
        
    def save(self, *args, **kwargs):
        self.price_per_month = self.morning_litres + self.evening_litres * price_per_litre * 30.00
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.total_litres = self.morning_litres + self.evening_litres
        super().save(*args, **kwargs)

    def get_total(self, *args, **kwargs):
        self.total = self.morning_litres + self.evening_litres * price_per_litre * 30.00
        super().save(*args, **kwargs)