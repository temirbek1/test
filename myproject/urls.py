from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from ladno.views import AuthorViewSet, BookViewSet, CategoryViewSet, ProductViewSet, ProfileViewSet, UserViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions  # Импортируйте permissions

# Создание и регистрация маршрутов для DRF ViewSets
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)

# Настройка Swagger документации
schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourproject.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),  # Используйте permissions из rest_framework
)

# Основные маршруты
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # Используйте router.urls для маршрутов API
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
