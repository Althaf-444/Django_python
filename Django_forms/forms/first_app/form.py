from django import forms

class Contect_form(forms.Form):
    name = forms.forms.CharField(max_length=100)
    Email = forms.forms.forms.EmailField()
    message = forms.forms.CharField(widget = forms.Textarea)
    
    def send_email(self):
        print(f"Send email from {self.cleaned_data['Email']} with message : {self.cleaned_data['message']}" )