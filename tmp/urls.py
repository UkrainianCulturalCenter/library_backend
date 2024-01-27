from django.urls import path, include
from rest_framework import routers
from tmp import views

app_name = "tmp"

router = routers.DefaultRouter()

router.register("temporary", views.TmpViewSet, basename="temporary")

urlpatterns = [path("", include(router.urls))]
