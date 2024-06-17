from django import forms
from .models import docreg, doclogin, nursereg, nurselogin, patientinfo, feedback

widgets = {
            'Password': forms.PasswordInput(),
            'Confirm_Password': forms.PasswordInput(), 
        }

class docregf(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(), label = 'Password')
    Confirm_Password = forms.CharField(widget=forms.PasswordInput(), label = 'Confirm Password')
    
    class Meta:
        model = docreg
        fields = ['Username', 'Password', 'Confirm_Password']
        
class docloginf(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(), label= "Password")
    
    class Meta:
        model = doclogin
        fields = ['Username', 'Password']
        
class nurseregf(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(), label = "Password")
    Confirm_Password = forms.CharField(widget=forms.PasswordInput(), label = "Confirm Password")
    
    class Meta:
        model = nursereg
        fields = ['Username', 'Password', 'Confirm_Password']

class nurseloginf(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(), label= "Password")
    
    class Meta:
        model = nurselogin
        fields = ["Username", "Password"]
        
class patientf(forms.ModelForm):
    
    class Meta:
        model = patientinfo
        fields = ["FirstName", "LastName", "Mobile"]
        
class feedbackf(forms.ModelForm):
    
    class Meta:
        model = feedback
        fields = ["Name", "Mobile", "Email", "Message"]

