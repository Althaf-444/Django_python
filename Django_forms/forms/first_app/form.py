from django import forms

class Contect_form(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':"form-control"}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control'}))
    
    def send_email(self):
        print(f"Send email from {self.cleaned_data['Email']} with message : {self.cleaned_data['message']}" )