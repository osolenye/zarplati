from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, AdminViewSet, WorkerViewSet, AdminRegistrationViewSet, ObtainTokenPairView, \
    WorkerRegistrationViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'workers', WorkerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/register/', AdminRegistrationViewSet.as_view({'post': 'create'})),
    path('worker/register/', WorkerRegistrationViewSet.as_view({'post': 'create'})),
    path('login/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
]
