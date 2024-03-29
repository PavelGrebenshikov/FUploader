from django import forms

OPTIONS = [
    ("r_spaces", "Remove spaces"),
    ("d_char", "Delete characters"),
    ("s_text", "Show text"),
]

class FileUploadOptionsForm(forms.Form):
    radio_button = forms.CharField(label="Available options", widget=forms.RadioSelect(choices=OPTIONS))


class FileUploadForm(forms.Form):
    input_file = forms.FileField(widget=forms.FileInput(attrs={'hidden':'hidden', 'id':'fileUpload'}))