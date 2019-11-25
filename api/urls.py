from django.urls import include, path
# from rest_framework import routers
from dynamic_rest import routers
from . import views
from .filterlists import InvestmentGuidelineOptionsByIGList

router_v1 = routers.DynamicRouter()
router_v1.register(r'investmentguidelines', views.InvestmentGuidelineViewSet)
router_v1.register(r'investmentguidelineoptions', views.InvestmentGuidelineOptionsViewSet)
router_v1.register(r'strategies', views.StrategyViewSet)
router_v1.register(r'strategists', views.StrategistViewSet)
router_v1.register(r'benchmarks', views.BenchmarkViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('v1/', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    # path('', views.investmentguidelines_list, name='ig_list'),
    # path('investmentguidelineoptions/ig/<int:ig>/', InvestmentGuidelineOptionsByIGList.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]