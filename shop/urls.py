from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/token/refresh', TokenRefreshView.as_view()),

    path('api/v1/categories/', views.CategoryList.as_view()),
    path('api/v1/categories/<int:pk>/', views.CategoryDetail.as_view()),
]

