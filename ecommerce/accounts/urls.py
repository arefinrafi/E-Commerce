from django.urls import path
from . import views
from .views import HomeView, ProductItemDetailView, add_to_cart, remove_from_cart

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('checkout/', views.checkout, name="checkout"),
    path('product/<slug>/', ProductItemDetailView.as_view(), name="product"),
    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', remove_from_cart, name="remove-from-cart"),
]
