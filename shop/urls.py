from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="DRF API",
        default_version="1.0.0",
        description="API documentation of the DRF API app",
    ),
    public=True,
)


urlpatterns = [
    path('api/docs', schema_view.with_ui('swagger', cache_timeout=0)),

    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/current_user/', views.current_user),
    path('api/v1/register/', views.register),
    path('api/v1/forgot_password/', views.forgot_password),
    path('api/v1/reset_password/<str:token>/', views.reset_password),
    path('api/v1/update_user_info/', views.update_user_info),

    path('api/v1/categories/', views.CategoryList.as_view(), name='category'),
    path('api/v1/categories/<int:pk>/', views.CategoryDetail.as_view(), name='category_details'),
]

