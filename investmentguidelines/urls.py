from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.investmentguidelines_list, name='ig_list'),
    path('ig/<int:pk>/', views.investmentguidelines_detail, name='ig_detail'),
    path('ig/<int:pk>/edit/', views.investmentguidelines_edit, name='ig_edit'),
    path('ig/new/', views.investmentguidelines_new, name='ig_new'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
]