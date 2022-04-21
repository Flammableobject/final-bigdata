from django import forms
from myapp.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fullname','address','postcode','email']