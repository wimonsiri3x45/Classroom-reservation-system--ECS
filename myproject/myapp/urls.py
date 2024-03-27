from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('userclassroom',views.userclassroom),
    path('reservationlist',views.reservationlist),
    path('booking',views.booking),
    path('deletebooking/<booking_id>',views.deletebooking),
]