
from rest_framework.routers import DefaultRouter

from api_user.views import *

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='users')
router.register(r'roles', RoleViewSet, basename='roles')
router.register(r'places', PlaceViewSet, basename='places')

urlpatterns = router.urls