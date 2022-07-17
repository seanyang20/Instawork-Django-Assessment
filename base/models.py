from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from multiselectfield import MultiSelectField



# Create your models here.
# Might not need this 

ROLE_CHOICE = ((1, 'Regular'),
               (2, 'Admin'))

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    phone = PhoneNumberField(null=False, blank=False, unique=True, region='US')
    role = MultiSelectField(choices=ROLE_CHOICE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return (self.first_name + self.last_name)
