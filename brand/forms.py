from django import forms

from . import models


class BrandForm(forms.ModelForm):
    brochure = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True})
    )
    location = forms.CharField()

    class Meta:
        model = models.Brand
        fields = "__all__"
