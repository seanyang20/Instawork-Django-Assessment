from django.forms import ModelForm
from django import forms
from .models import Member
from django.forms.widgets import RadioSelect

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={"placeholder": "First Name",}
            ),
            'last_name': forms.TextInput(attrs={"placeholder": "Last Name",}
            ),
            'email': forms.TextInput(attrs={"placeholder": "Email",}
            ),
            'phone': forms.TextInput(attrs={"placeholder": "Phone Number",}
            ),
            'role': forms.RadioSelect()
        } 