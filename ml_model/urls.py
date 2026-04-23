from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),               # Serves the HTML at /api/
    path('predict/', views.predict_sentiment, name='predict'), # The JSON API
]