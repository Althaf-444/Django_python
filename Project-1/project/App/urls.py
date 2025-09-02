from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('create/' , views.create_view , name = 'create'),
    path('list' , views.read_view , name = 'list'),
    path('update/<int:product_id>/' , views.update_view , name = 'update'),
    path('delete/<int:product_id>/' , views.delete_view , name = 'delete'),
]
