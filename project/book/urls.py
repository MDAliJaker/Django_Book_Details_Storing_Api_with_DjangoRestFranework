from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookList.as_view(), name='book-list'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
]