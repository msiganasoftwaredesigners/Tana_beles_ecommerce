from django.urls import path
from .views import MakePaymentView, payment_notification
from .views import PaymentPageView


urlpatterns = [
    
    path('', MakePaymentView.as_view(), name='make_payment'),
    path('payment_notification/', payment_notification, name='payment_notification'),
    path('payment_page/', PaymentPageView.as_view(), name='payment_page')
]
