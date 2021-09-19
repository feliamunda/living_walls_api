from .views import AssetViewSet
from django.urls import path

urlpatterns = [
    path('', AssetViewSet.as_view({'get':'list','post':'create'})),
    path('<pk>', AssetViewSet.as_view({'get':'retrieve','patch':'partial_update'})),
]