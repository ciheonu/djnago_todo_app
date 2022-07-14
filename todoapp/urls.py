from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete_item/<int:pk>', views.delete, name='delete'),
    path('update_item<int:pk>', views.update, name='update'),
]
