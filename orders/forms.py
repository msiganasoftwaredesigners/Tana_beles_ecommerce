from django import forms

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    order_phone = forms.CharField(max_length=13, required=False)
    order_email = forms.EmailField(max_length=50, required=False)
    order_address = forms.CharField(max_length=100, required=True)
    referral_code = forms.CharField(max_length=30, required=False)
    