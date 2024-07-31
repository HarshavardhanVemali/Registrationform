from django.contrib import admin
from django.urls import path
from registrationformapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('submit_registration/',views.submit_registration,name='submit_registration'),
]
