from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostView)
router.register('comments', views.CommentView)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('current_user/', views.current_user),
    path('register/', views.register),
    path('forgot_password/', views.forgot_password),
    path('reset_password/<str:token>/', views.reset_password_view),
    path('reset_password/', views.reset_password),
    path('update_user_info/', views.update_user_info),

    path('categories/', views.CategoryList.as_view(), name='category'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category_details'),

    path('', include(router.urls)),
]

