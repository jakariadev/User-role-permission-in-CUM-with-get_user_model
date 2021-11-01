from django.urls import path
from .views import SignupPageView, BooksView
urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('books/', BooksView, name='books'),
]
