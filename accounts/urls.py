from django.urls import path
from . import views
urlpatterns=[

    
    path('send-otp/', views.send_otp, name='send_otp'),
    #path('verify-otp/', views.verify_otp, name='verify_otp'),
     path('register/', views.register, name='register'),
     path('login/', views.user_login, name='login'),
     path('dashbaord/', views.dashboard, name='dashboard'),
     path('logout/', views.user_logout, name='logout'),
]