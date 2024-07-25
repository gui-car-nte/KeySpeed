from rest_framework import routers
from .views import UserViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register('User', UserViewSet, 'user_api')
urlpatterns = router.urls