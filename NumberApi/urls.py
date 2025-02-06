from django.urls import re_path
from .views import NumberApi

urlpatterns = [
    re_path(r'^api/classify-number/?$', NumberApi.as_view(), name='classify_number'),
]
