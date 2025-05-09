from django.urls import path
from main import views
from .views import ProductDetail
# Ссылки на страницы
urlpatterns = [
    path('', views.StorePage,name='StorePage'),
    path('product/<int:pk>/', ProductDetail, name='ProductDetail'),
]