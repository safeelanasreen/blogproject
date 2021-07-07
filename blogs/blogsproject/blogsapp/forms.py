from . models import blogs
from django import forms
class ModeForm(forms.ModelForm):
    class Meta:
        model=blogs
        fields=['name','desc','img']