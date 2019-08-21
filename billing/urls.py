from django.urls import path
from . import views

urlpatterns = [
    path('createinvoice/', views.BillHeaderCreate.as_view(), name = 'createinvoice'),
    path('createinvoice/<int:pk>', views.UpdateBillHeader.as_view(), name = 'updateinvoice'),
]
