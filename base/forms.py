from django.forms import ModelForm
from django import forms
from .models import Member
from django.forms.widgets import RadioSelect

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'role': forms.RadioSelect()
        } 