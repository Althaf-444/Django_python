from django.urls import path
from . import views

urlpatterns = [
    path('', views.contect,name='home'),
    path('contect/', views.contect_viwe , name= 'contect'),
    path('contect/succsess', views.contect_success , name = 'content-success'),
    

]
