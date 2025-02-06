from django.urls import path
from .views import NumberApi

urlpatterns = [
    path('api/classify-number/', NumberApi.as_view(), name='classify_number'),
]
