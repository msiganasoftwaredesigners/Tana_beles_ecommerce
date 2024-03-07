from django.urls import path
from .views import MakePaymentView, payment_notification

app_name = 'telebirrpay'

urlpatterns = [
    
    path('', MakePaymentView.as_view(), name='make_payment'),
    path('payment_notification/', payment_notification, name='payment_notification'),
]
