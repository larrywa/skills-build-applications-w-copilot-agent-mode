"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import HttpResponse
import os
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

def root_view(request):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    codespace_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
    html = f"""
        <h1>Welcome to Octofit Tracker API</h1>
        <p>Codespace URL: <a href='{codespace_url}'>{codespace_url}</a></p>
        <p>Visit <a href='/api/'>/api/</a> for REST endpoints.</p>
    """
    return HttpResponse(html)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboards', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
