from django.urls import path
from .views import *

urlpatterns = [
    path('', SupportCreateDelivery.as_view(), name="main"),
    path('create/<int:pk>/', CreateDelivery.as_view(), name="create")
]
