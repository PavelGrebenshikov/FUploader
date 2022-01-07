from django import forms


class FileUploadForm(forms.Form):
    input_file = forms.FileField(widget=forms.FileInput(attrs={'hidden':'hidden', 'id':'fileUpload'}))