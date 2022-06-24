from django.urls import path
from .views import blogCreateView

urlpatterns = [
    path('', blogCreateView.as_view(), name='home'),
]
