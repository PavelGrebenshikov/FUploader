from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .service import ProcessingText


def index(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            content = ProcessingText(request.FILES["input_file"]).get_content()
            print(content)
            return render(request, 'main/main.html',
             {"text": content["decode"], "length": content["length"]})
    else:
        form = FileUploadForm()
    return render(request, 'main/index.html', {'form': form})