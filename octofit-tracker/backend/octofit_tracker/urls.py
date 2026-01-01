import os

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from octofit_tracker.views import (
    ActivityViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    UserViewSet,
    WorkoutViewSet,
)

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)


@api_view(['GET'])
def api_root(request):
    return Response({'base_url': base_url})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='home'),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
