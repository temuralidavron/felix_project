from django.urls import path
from .views import WarehouseAPI

urlpatterns = [
    path('api/v1/warehouse-request/', WarehouseAPI.as_view(), name='production_request'),
]
