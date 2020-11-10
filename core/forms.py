from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Deposito Bancario'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'barrio....',
        'class': 'form-control'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Casa ó departamento...',
        'class': 'form-control'
    }))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'

    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Codigo Promocional'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()
