from rest_framework.routers import DefaultRouter

from .views import TutorialView

router = DefaultRouter()
router.register("tutorials",TutorialView)

urlpatterns = router.urls

