from django.contrib import admin
from django.urls import path

from .views import (BBLoginView, BBLogoutView, BBPasswordChangeView,
                    ChangeUserInfoView, RegisterDoneView, RegisterUserView,
                    DeleteUserView,
                    index, other_page, profile, user_activate, by_rubric, detail,
                    profile_bb_detail, profile_bb_add, profile_bb_change, profile_bb_delete,
                    redirect_view)

app_name = 'main'
urlpatterns = [
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/change/<int:pk>/', profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/delete/<int:pk>/', profile_bb_delete, name='profile_bb_delete'),
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/<int:pk>/', profile_bb_detail, name='profile_bb_detail'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout' ),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/асtivate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>', other_page, name='other'),
    path('<int:rubric_pk>/<int:pk>/<str:url>', redirect_view),
    path('', index, name='index'),
]
