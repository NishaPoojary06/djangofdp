from django import forms
class inputforms(forms.Form):
    name=forms.CharField(max_length=10)
    clg=forms.CharField(max_length=10,label="Enter your college")
    crs=forms.CharField(max_length=10,label="Enter the course name")
    
    