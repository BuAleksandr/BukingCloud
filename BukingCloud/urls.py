"""BukingCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from BukingCloud.cloud.views.user_view import RegistrUserView, get_detail_user_list, delete_user
from BukingCloud.cloud.views.file_views import FileView
from BukingCloud.cloud.views.auth_view import login_view, get_csrf_token, me_view, logout_view
from BukingCloud.cloud.views.file_transfer_view import get_link, get_file


urlpatterns = [
    path('api/auth/login/', login_view),
    path('api/auth/logout/', logout_view),
    path('api/auth/get_csrf/', get_csrf_token),
    path('api/auth/me/', me_view),
    path('api/detail_users_list/', get_detail_user_list),
    path('api/delete_user/<int:user_id>/', delete_user),
    path('api/registr/', RegistrUserView.as_view()),
    path('api/files/', FileView.as_view()),
    path('api/link/', get_link),
    path('api/link/<str:link>/', get_file),
    path('', include('frontend.urls')),
]