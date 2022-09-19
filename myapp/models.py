from django.db import models


class CloudFile(models.Model):
    description = models.CharField(max_length=200)
    upload_date = models.DateTimeField('date uploaded')
    file = models.FileField(upload_to='uploads/')
