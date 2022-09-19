from .models import CloudFile
from rest_framework import serializers


class CloudFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CloudFile
        fields = ['description', 'upload_date', 'file']

