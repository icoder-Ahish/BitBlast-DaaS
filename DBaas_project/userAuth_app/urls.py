from django.contrib import admin
from django.urls import path,include
from userAuth_app.views import UserAuthViewSet, LoginViewSet,AddRoleViewset
from rest_framework import routers
# from . import views


router = routers.DefaultRouter()
router.register(r'users', UserAuthViewSet, basename="register")

router.register(r'login', LoginViewSet, basename='login')
router.register(r'add_roles_to_user', AddRoleViewset, basename='add_roles_to_user')


urlpatterns = [
    
    path("", include(router.urls)),
   
    
]