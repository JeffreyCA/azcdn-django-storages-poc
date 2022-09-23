from django.urls import path

from . import views

urlpatterns = [
    path("test", views.SingleCloudFileViewSet.as_view({'get': 'retrieve'})),
]
