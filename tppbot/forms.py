from django import forms

from .models import *

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('store_name','category',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('uuid','create_date',)

class CodeMasterForm(forms.ModelForm):
    class Meta:
        model = CODE
        fields = ('name','super')