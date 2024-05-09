from django import forms
class inputforms(forms.Form):
    input1=forms.IntegerField(min_value=0,max_value=30,label="Enter starting number",required=False)
    input2=forms.IntegerField(min_value=0,max_value=30,label="Enter ending number",required=False)