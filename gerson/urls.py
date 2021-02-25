from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('new', views.post_new, name='new'),
]
