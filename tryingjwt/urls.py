from django.db.models import fields
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

urlpatterns = [
    path('' , views.index , name="home"),
    path('api/token/' , jwt_views.TokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('api/token/refresh/' , jwt_views.TokenRefreshView.as_view() , name='token_refresh'),
    path('hello/' , views.HelloView.as_view() , name="hello")
]