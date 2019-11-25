from core.models import InvestmentGuidelineOptions
from .serializers import InvestmentGuidelineOptionsSerializer
from rest_framework import generics


class InvestmentGuidelineOptionsByIGList(generics.ListAPIView):
    serializer_class = InvestmentGuidelineOptionsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the investmentguidelineoptions for
        a specific investmentguideline as determined by the ig portion of the URL.
        """
        queryset = InvestmentGuidelineOptions.objects.all()
        ig = self.request.query_params.get('ig', None)
        if ig is not None:
            queryset = queryset.filter(investmentguideline_id=ig)
        return queryset