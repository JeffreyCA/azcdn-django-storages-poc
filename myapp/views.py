from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CloudFileSerializer
from .models import CloudFile

class CloudFileViewSet(viewsets.ModelViewSet):
    queryset = CloudFile.objects.all().order_by('-upload_date')
    serializer_class = CloudFileSerializer
