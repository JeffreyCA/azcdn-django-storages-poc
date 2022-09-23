from django.http import HttpResponse, FileResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CloudFileSerializer
from .models import CloudFile

class CloudFileViewSet(viewsets.ModelViewSet):
    queryset = CloudFile.objects.all()
    serializer_class = CloudFileSerializer

class SingleCloudFileViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        file1 = CloudFile.objects.get(id=2)
        print(file1)
        return FileResponse(file1.file, as_attachment=True)
