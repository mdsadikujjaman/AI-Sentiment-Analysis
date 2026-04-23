"""
URL configuration for new project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse # <-- Import this

# Create a quick function for the homepage
def home(request):
    return HttpResponse("Welcome to the ML Predictor Homepage! Go to /api/predict/ to see the API.")

urlpatterns = [
    path('', home, name='home'), # <-- Add this line for the empty path
    path('admin/', admin.site.urls),
    path('api/', include('ml_model.urls')),
]