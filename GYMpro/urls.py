"""
URL configuration for GYMpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from GYMapp.views import EMViewSet, LogViewSet , customToken
from GYMapp import views
from rest_framework.routers import DefaultRouter
#from GYMapp.views import  CustomTokenObtainPairView
#from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView )
#from rest_framework_simplejwt.views import TokenVerifyView

router = DefaultRouter(trailing_slash=False)
router.register(r'Em',EMViewSet, basename='Em')
router.register(r'log',LogViewSet, basename='log')
router.register(r'custom_token',customToken, basename='custom_token')
# router.register(r'token', CustomTokenObtainPairView , basename='token' )

urlpatterns = [
    path("admin/", admin.site.urls),
    path('em/',include(router.urls)),
    path('Signup' , views.SignUp ),
    path('login' , views.Login),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # explore it after some time
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #path('api/custom_token', CustomTokenObtainPairView.as_view(), name='custom_token')
]
