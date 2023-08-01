from django import forms
from .models import Upload


class UploadForm(forms.ModelForm) :
    class meta() :
        model = Upload
        fields = ["name", "mfile", "category"]



