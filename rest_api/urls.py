from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, AdminViewSet, WorkerViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'workers', WorkerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]