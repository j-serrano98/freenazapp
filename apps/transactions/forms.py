from django import forms
from .models import Transaction, TransactionCategory, PaymentMethod
import datetime


class TransactionForm(forms.ModelForm):
    status_choices = Transaction.StatusChoices.choices

    status = forms.ChoiceField(
        choices=status_choices,
        initial=Transaction.StatusChoices.SUCCESSFUL,
        required=True,
    )

    class Meta:
        model = Transaction
        fields = ['type', 'currency', 'amount', 'tax', 'name', 'description', 'method', 'category', 'status']
        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': '765.65'}),
            'tax': forms.TextInput(attrs={'placeholder': '3.15'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name of the transaction'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description of the transaction'}),
            'type': forms.Select(attrs={'id': 'id_type'})

        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['method'].empty_label = "Select a payment method"
        self.fields['category'].empty_label = "Select category"
        self.fields['status'].empty_label = None
        
        if user is not None:
            self.fields['method'].queryset = PaymentMethod.objects.filter(user=user)
            self.fields['category'].queryset = TransactionCategory.objects.filter(user=user)

class TransactionCategoryForm(forms.ModelForm):
    class Meta:
        model = TransactionCategory
        fields = ['name', 'type']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance