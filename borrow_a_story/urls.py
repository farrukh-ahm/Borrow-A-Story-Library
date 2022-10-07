from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookCatalogue.as_view(), name='home'),
    path('book_issue/<slug:slug>/', views.BookIssue.as_view(), name='book_issue'),
    path('book_return/<slug:slug>/', views.BookReturn.as_view(), name='book_return')
]