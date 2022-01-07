from django.db import models

# Create your models here.

class FileUploadModel(models.Model):
    file = models.FileField("File name", upload_to="")