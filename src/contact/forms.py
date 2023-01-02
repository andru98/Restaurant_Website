from django import forms

class ContactForm(forms.Form):
    Subject = forms.CharField()
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget= forms.Textarea, required= True)

 