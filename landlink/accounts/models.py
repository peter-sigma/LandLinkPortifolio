from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
class CustomUser(AbstractUser):
        USER_TYPES = [
                        ('buyer', 'Buyer'),
                        ('seller', 'Seller'),
                        ('lawyer', 'Lawyer'),
                    ]
        user_type = models.CharField(max_length=10, choices=USER_TYPES)
        groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
                                                    )
        user_permissions = models.ManyToManyField(
                    Permission,
                    related_name='custom_user_set',
                    blank=True,
                    help_text='Specific permissions for this user.',
                    verbose_name='user permissions',
                )
