from django import forms

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20)
    order_phone = forms.CharField(max_length=13, required=True)
    order_email = forms.EmailField(max_length=50, required=False)
    order_address = forms.CharField(max_length=100, required=True)
    