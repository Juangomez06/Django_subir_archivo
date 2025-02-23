from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True) 
    uploadedFile = models.FileField(upload_to="Uploaded_Files/") 
    dateTimeOfUpload = models.DateTimeField(auto_now=True) 