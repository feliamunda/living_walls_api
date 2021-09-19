from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import AssetSerializer
from .models import Asset

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer