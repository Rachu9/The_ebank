from django import forms
from .models import Transaction, BillPayment,Account

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['receiver', 'amount']
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['receiver'].queryset = Account.objects.exclude(user=user)

# class BillPaymentForm(forms.ModelForm):
#     class Meta:
#         model = BillPayment
#         fields = ['account', 'amount', 'bill_type']
#         widgets = {
#             'account': forms.Select(attrs={'class': 'form-control'}),
#             'amount': forms.NumberInput(attrs={'class': 'form-control'}),
#             'bill_type': forms.TextInput(attrs={'class': 'form-control'}),
#         }
# class BillPaymentForm(forms.ModelForm):
#     class Meta:
#         model = BillPayment
#         fields = ['account', 'amount', 'bill_type']
#         widgets = {
#             'account': forms.Select(attrs={'class': 'form-control'}),
#             'amount': forms.NumberInput(attrs={'class': 'form-control'}),
#             'bill_type': forms.TextInput(attrs={'class': 'form-control'}),
#         }


# class BillPaymentForm(forms.ModelForm):
#     class Meta:
#         model = BillPayment
#         fields = ['account', 'amount', 'bill_type']
#         widgets = {
#             'account': forms.Select(attrs={'class': 'form-control'}),
#             'amount': forms.NumberInput(attrs={'class': 'form-control'}),
#             'bill_type': forms.TextInput(attrs={'class': 'form-control'}),
#         }


class BillPaymentForm(forms.ModelForm):
    class Meta:
        model = BillPayment
        fields = ['account', 'amount', 'bill_type']
        widgets = {
            'account': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'bill_type': forms.TextInput(attrs={'class': 'form-control'}),
        }