from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name= 'home'),
    path('login/',views.login_viwe,name= 'login'),
    path('logout/',views.logout_viwe,name= 'logout'),
    path('registration/',views.register_viwe,name= 'registration'),
]
