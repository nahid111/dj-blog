from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostView)
router.register('comments', views.CommentView)


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', views.UserRegisterView.as_view()),
    path('forgot_password/', views.forgot_password),
    path('reset_password/<str:token>/', views.reset_password_view),
    path('reset_password/', views.reset_password),
    path('user/current', views.UserCurrentView.as_view()),
    path('categories/', views.CategoryList.as_view(), name='category'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category_details'),

    path('', include(router.urls)),
]

