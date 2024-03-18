from django.urls import path
from .views import MakePaymentView, payment_notification
from .views import payment_page


urlpatterns = [
    
    path('', MakePaymentView.as_view(), name='make_payment'),
    path('payment_page/', payment_page, name='payment_page'),
    path('payment_notification/', payment_notification, name='payment_notification'),
]