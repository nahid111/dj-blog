from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

router = routers.DefaultRouter()
router.register('comments', views.CommentView)

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('token/', TokenObtainPairView.as_view(), name='sign-in'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('sign-up/', views.UserSignUpView.as_view(), name='sign-up'),

    path('password/forgot/', views.password_forgot, name='password-forgot'),
    path('password/reset/<str:token>/', views.password_reset_form_view, name='password-reset-form'),
    path('password/reset/', views.password_reset, name='password-reset'),

    path('users/current/', views.UserCurrentView.as_view(), name='current-user'),

    path('categories/', views.CategoryList.as_view(), name='category'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category_details'),

    path('posts/', views.PostList.as_view(), name='post'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_details'),

    path('', include(router.urls)),
]
