from django.urls import path

from .views import InvoiceView

urlpatterns = [
    path('create/', InvoiceView.as_view(), name='create-invoice'),
]