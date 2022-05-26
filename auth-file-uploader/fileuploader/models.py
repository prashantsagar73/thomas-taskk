from django.db import models
from datetime import datetime


# Create your models here.

class Fileupload(models.Model):
    file_name = models.CharField(max_length = 50)
    Main_File = models.FileField(upload_to='mydocuments/') 
    upload_at = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return f'{self.file_name}'