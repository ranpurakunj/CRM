from rest_framework.routers import DefaultRouter

from Profile.viewsets import ProfileViewSet

router = DefaultRouter()
router.register('profiles-abc', ProfileViewSet, 
basename="profile")
print(router.urls)
urlpatterns = router.urls
