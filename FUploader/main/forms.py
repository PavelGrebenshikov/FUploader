from django import forms

OPTIONS = [
    ("d_space", "Delete Space"),
    ("d_symbols", "Delete Symbols"),
    ("f_text", "format text"),
]

class FileUploadOptionsForm(forms.Form):
    radio_button = forms.CharField(label="Available options", widget=forms.RadioSelect(choices=OPTIONS))


class FileUploadForm(forms.Form):
    input_file = forms.FileField(widget=forms.FileInput(attrs={'hidden':'hidden', 'id':'fileUpload'}))