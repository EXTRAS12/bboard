from django.contrib import admin
from django.urls import path

from .views import (BBLoginView, BBLogoutView, BBPasswordChangeView,
                    ChangeUserInfoView, RegisterDoneView, RegisterUserView,
                    index, other_page, profile)

app_name = 'main'
urlpatterns = [
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout' ),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('<str:page>', other_page, name='other'),
    path('', index, name='index'),
]
