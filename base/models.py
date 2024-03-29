from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from multiselectfield import MultiSelectField
from django.forms.widgets import RadioSelect
from phonenumbers import PhoneNumberFormat



# Create your models here.
# Might not need this 

ROLE_CHOICE = (("1", "Regular - Can't delete members"),
               ("2", "Admin - Can delete members"))

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    phone = PhoneNumberField(null=False, blank=False, unique=True, region='US')
    # role = MultiSelectField(choices=ROLE_CHOICE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICE, default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return (self.first_name + self.last_name)
