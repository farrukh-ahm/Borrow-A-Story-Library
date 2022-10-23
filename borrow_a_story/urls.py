from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookCatalogue.as_view(), name='home'),
    path('book_issue/<slug:slug>/', views.BookIssue.as_view(), name='book_issue'),
    path('issued/<slug:slug>', views.BookIssue.as_view(), name='issued'),
    path('book_return/<slug:slug>/', views.BookReturn.as_view(), name='book_return'),
    path('profile/', views.UserProfile.as_view(), name='user_profile'),
    path('bookmarked/<slug:slug>', views.Bookmark.as_view(), name='bookmarked_books'),
    path('test/', views.Test.as_view(), name='test'),
]