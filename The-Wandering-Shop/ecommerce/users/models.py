from django.db import models

from django.contrib.auth.models import User

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    class Meta:
        ordering = ('last_name', 'first_name')  # orders profiles by first then last name
        verbose_name_plural = 'User Profiles' 
        db_table = 'User Profile' 

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()
