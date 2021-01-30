from django.contrib import admin
from django.urls import path,include
from mysite import views

urlpatterns = [
    # Social all-auth Rest Framework
    path('accounts/', include('allauth.urls')),

    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('user_logout',views.user_logout),
    path('updateprofile/',views.updateprofile),
    
]
