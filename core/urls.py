from django.conf import settings
from django.urls import path, include
from .views import InvestmentGuidelineCreate, BenchmarkCreate
from . import views

ig_root = 'investmentguidelines'
bm_root = 'benchmarks'

urlpatterns = [
    path('', views.indexview, name='main'),
    path(bm_root + '/', views.benchmarks_list, name='bm_list'),
    path(bm_root + '/new/', views.benchmark_new, name='bm_new'),
    path(bm_root + '/<int:pk>/', views.benchmark_detail, name='bm_detail'),
    path(bm_root + '/<int:pk>/edit/', views.benchmark_edit, name='bm_edit'),
    path(ig_root + '/', views.investmentguidelines_list, name='ig_list'),
    path(ig_root + '/<int:pk>/', views.investmentguidelines_detail, name='ig_detail'),
    path(ig_root + '/new/', InvestmentGuidelineCreate.as_view(), name='ig_new'),
    path(ig_root + '/<int:pk>/edit/', views.investmentguidelines_edit, name='ig_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
