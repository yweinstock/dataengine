from django.urls import path, include


urlpatterns = [
    path('', include('lbworkflow.urls')), # url for lbworkflow
    path('attachment/', include('lbattachment.urls')), # url for lbattachment
]