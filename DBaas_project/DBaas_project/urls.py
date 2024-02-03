# project/urls.py
from django.contrib import admin
from django.urls import path, include  # Import the include function
from project_api.views import get_projects_by_user, get_clusters_by_user, get_clusters_by_project, ProjectViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('userAuth_app.urls')),
    path("api/v2/", include('project_api.urls')),
    path("api/v3/", include('provider1_api.urls')),
    path("api/v2/project/user/<int:user_id>/", get_projects_by_user, name='get_projects_by_user'),
    path("api/v2/cluster/user/<int:user_id>/", get_clusters_by_user, name='get_clusters_by_user'),
    path("api/v2/cluster/project/<int:project_id>/", get_clusters_by_project, name='get_clusters_by_project'),
    path('', include('django_prometheus.urls')),
    path("api/v2/project/<int:pk>/rename/", ProjectViewSet.as_view({'put': 'rename_project'}), name='rename-project'),
]
