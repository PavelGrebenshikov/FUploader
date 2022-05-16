from django.shortcuts import render, redirect
from .forms import FileUploadForm, FileUploadOptionsForm
from .service import processong_text


def index(request):
    if request.method == 'POST':
        options_form = FileUploadOptionsForm(request.POST)
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid() or options_form.is_valid():
            try:
                get_option = request.POST['radio_button']
                get_file = request.FILES["input_file"]
                content = processong_text(get_file, get_option)
                return render(request, 'main/main.html', {"text": content})
            except TypeError:
                redirect("home")
    else:
        options_form = FileUploadOptionsForm()
        form = FileUploadForm()
    return render(request, 'main/index.html', {'form': form, 'options_form': options_form})