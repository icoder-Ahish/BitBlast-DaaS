from django.contrib import admin
from django.urls import path, include
from project_api.views import ProjectViewSet, ClusterViewSet, ClusterDeleteViewSet, get_projects_by_user, display_artifacts, get_variables, ContentByClusterNameView, display_clusters

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cluster', ClusterViewSet, basename="cluster")
router.register(r'deletecluster', ClusterDeleteViewSet, basename="cluster1")
router.register(r'project', ProjectViewSet, basename='project')

urlpatterns = [
    path('api/v2/project/user/<int:user_id>/', get_projects_by_user, name='get_projects_by_user'),
    path('display_clusters/', display_clusters, name='display_clusters'),
   
    path('get_pipeline_status/', ClusterViewSet.as_view({'get': 'get_pipeline_status'}), name='get-pipeline-status'),
    path('display_artifacts/', display_artifacts, name='display_artifacts'),
    path('get_variables/', get_variables, name='get_variables'),
    path('result/content/<str:cluster_name>/', ContentByClusterNameView.as_view(), name='content-by-cluster-name'),
    
    # New URL for checking if a cluster name already exists
    path('api/v2/cluster/check_cluster_exists/', ClusterViewSet.as_view({'get': 'check_cluster_exists'}), name='check-cluster-exists'),
    path("api/v2/project/<int:pk>/rename/", ProjectViewSet.as_view({'put': 'rename_project'}), name='rename-project'),
    path("", include(router.urls)),
]
