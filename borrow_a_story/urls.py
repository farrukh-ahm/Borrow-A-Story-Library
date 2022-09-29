from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookCatalogue.as_view(), name='home'),
]