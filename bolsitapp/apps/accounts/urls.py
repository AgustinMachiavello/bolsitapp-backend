from django.urls import path, include
from rest_framework import routers

from .views.users import UserViewSet

routerUsers = routers.DefaultRouter()
routerUsers.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(routerUsers.urls)),
    path('auth/', include('rest_framework.urls'))
]
