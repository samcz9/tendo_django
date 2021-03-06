"""tendo_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rest_framework_views
from tendo_django.core.views import FeedbackSurveyViewSet
api_v1_router = DefaultRouter(trailing_slash=False)
api_v1_router.register(r'surveys', FeedbackSurveyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1_router.urls))
]
