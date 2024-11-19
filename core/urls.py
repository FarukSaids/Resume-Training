from django.urls import path

from DjangoResume.urls import urlpatterns
from .views import index

urlpatterns = [
    path('', index, name='index'),
]