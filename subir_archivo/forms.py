from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'uploadedFile']
        
class UploadFileForm(forms.Form):
    file = forms.FileField(label="Selecciona un archivo TXT")