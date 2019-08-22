from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.BillHeaderCreate.as_view(), name = 'createinvoice'),
    path('edit/<int:pk>', views.UpdateBillHeader.as_view(), name = 'editinvoice'),
    path('', views.BillListView.as_view(), name = 'billinghome')
]
