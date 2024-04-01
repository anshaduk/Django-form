from django import forms
from .models import user

class student(forms.ModelForm):
    # name=forms.CharField(max_length=100)
    # email=forms.EmailField()
    # password=forms.CharField(max_length=10)
    class Meta:
        model=user
        fields=['name','email','password']
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(attrs={'class':'form-control'})
    }