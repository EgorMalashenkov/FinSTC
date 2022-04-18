from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"car", views.CarModelViewSet, basename="Car")
urlpatterns = router.urls
