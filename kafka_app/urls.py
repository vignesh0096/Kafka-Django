from django.urls import path
from .views import *

urlpatterns = [
    path('ProducerAPI/', ProducerAPI.as_view()),
    path('ConsumerAPI/', ConsumerAPI.as_view()),
    path('CategoriesAPI/', CategoriesAPI.as_view()),
]