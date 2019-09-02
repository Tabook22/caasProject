from django.urls import path, include
from django.views import generic

urlpatterns = [
    path('',generic.TemplateView.as_view(template_name="pages/index.html"))
]
