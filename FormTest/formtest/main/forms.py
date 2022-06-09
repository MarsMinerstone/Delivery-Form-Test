from .models import *
from django import forms


class SupportAddDeliveryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Choose Category"
        self.fields['p_image'].required = False

    class Meta:
        model = Product
        fields = ["prod_name", "p_image", "cat"]


class SupportChooseDeliveryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivery_name'].empty_label = "Choose Product"

    class Meta:
        model = Delivery
        fields = ["delivery_name"]
