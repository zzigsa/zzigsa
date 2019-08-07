from django import forms
from photographer.models import ProductRegistration

class UploadForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = ProductRegistration
        fields = ['title', 'pub_date', 'summary', 'image', 'detail']