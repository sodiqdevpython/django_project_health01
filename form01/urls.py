from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='form01'),
    path('addform', views.form01, name='addform'),
]