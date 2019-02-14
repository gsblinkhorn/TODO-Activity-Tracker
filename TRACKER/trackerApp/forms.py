from django import forms
from .models import List

class ListForm(forms.ModelForm):

    subject = forms.CharField(required=False)
    isCompleted = forms.BooleanField(required=False)
    date = forms.DateField(required=False)
    
    class Meta:
        model = List
        fields = ["activity", "subject", "isCompleted", "date"]