from django.urls import include, path
# from rest_framework import routers
from dynamic_rest import routers
from . import views
from .filterlists import InvestmentGuidelineOptionsByIGList

router = routers.DynamicRouter()
router.register(r'investmentguidelines', views.InvestmentGuidelineViewSet)
router.register(r'investmentguidelineoptions', views.InvestmentGuidelineOptionsViewSet)
router.register(r'strategies', views.StrategyViewSet)
router.register(r'strategists', views.StrategistViewSet)
router.register(r'benchmarks', views.BenchmarkViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('', views.investmentguidelines_list, name='ig_list'),
    # path('investmentguidelineoptions/ig/<int:ig>/', InvestmentGuidelineOptionsByIGList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]