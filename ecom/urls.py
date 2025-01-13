from django.contrib import admin
from django.urls import path,include
from accounts import views
urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('',views.landing_page,name='landing_page'),

    path('accounts/',include('accounts.urls')),#all logingin handle and ragistertion of user is here 
]
