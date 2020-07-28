from django import forms

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = form.BooleanField(required=False, initial=False, widget=forms.HiddenInput)