"""ebook_repository_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from ebook_repository.views import (
    CategoryViewSet,
    EBookViewSet,
    ExtractMetadataView,
    FiltersView,
    LanguageViewSet,
    UserViewSet,
)
from extensions.simplejwt import EBookRepositoryObtainPairView

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("ebooks", EBookViewSet)
router.register("languages", LanguageViewSet)
router.register("categories", CategoryViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token", EBookRepositoryObtainPairView.as_view()),
    path("api/token/refresh", TokenRefreshView.as_view()),
    path("api/filters", FiltersView),
    path("api/metadata", ExtractMetadataView)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
