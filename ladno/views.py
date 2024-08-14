from rest_framework import viewsets
from .models import Author, Book, Category, Product, Profile
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer, ProductSerializer, ProfileSerializer, UserSerializer
from django.contrib.auth.models import User

# Views для моделей Один ко Многим
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Views для моделей Многие ко Многим
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Views для моделей Один к Одному
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
